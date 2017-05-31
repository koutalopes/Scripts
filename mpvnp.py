# -*- coding: utf-8 -*-

	# mpv "now playing" para o weechat
	# Ricardo Lopes (Kouta_Kun)
	#
	# v0.5.1

	# Adicionar ao mvp.conf a linha:
	#   input-ipc-server=/tmp/mpvsocket
	#

# Importar bibliotecas
import socket
import json
import datetime
import subprocess
import sys
import weechat as w

reload(sys)
sys.setdefaultencoding('utf-8')

# Informações de registro do script
SCRIPT_NAME	= "mpvnp"
SCRIPT_AUTHOR 	= "Kouta_Kun"
SCRIPT_VERSION	= "0.5.1"
SCRIPT_LICENSE	= "Copyleft"
SCRIPT_DESC	= "mpv Now playing"

MPVSOCK = "/tmp/mpvsocket"

def hdata(message):
	i = str(message)
	msg = float(i.split(".")[0])

	return msg

def pbar(progress):
	barLength = 14 # Modify this to change the length of the progress bar
	status = ""
	if isinstance(progress, int):
		progress = float(progress)

	if not isinstance(progress, float):
		progress = 0
		status = "error: progress var must be float\r\n"

	block = int(round(barLength*(progress/100)))
	text = "[{0}]".format( "#"*block + "-"*(barLength-block))

	return text

# def obr(path):
# 	cmd = "mediainfo"
# 	args = "--Output=General;%OverallBitRate/String%"
# 	o = subprocess.check_output([cmd, args, path]).decode("UTF-8")
#
# 	if len(o.split()) == 3:
# 		if o.split()[2] == "Mbps":
# 			obr = "~" + o.split()[0] + o.split()[1] + " Mb/s"
# 		else:
# 			obr = "~" + o.split()[0] + o.split()[1] + " Kb/s"
# 	elif len(o.split()) == 2:
# 		if o.split()[1] == "Mbps":
# 			obr = "~" + o.split()[0] + " Mb/s"
# 		else:
# 			obr = "~" + o.split()[0] + " Kb/s"
#
# 	return obr

def fsize(size):
	if (len(str(size))) == 10:
		s = (float(size) / 1073741824)
		s = round(s, 2)
		sd = str(s) + " Gb"
	else:
		s = (float(size) / 1048576)
		s = round(s, 2)
		sd = str(s) + " Mb"

	return sd

def getInfos():
	sock.sendall(str.encode('{"command":["get_property","filename"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	filename = data["data"]

	sock.sendall(str.encode('{"command":["get_property","percent-pos"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	percent = hdata(data["data"])

	sock.sendall(str.encode('{"command":["get_property","time-pos"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	timepos = hdata(data["data"])

	sock.sendall(str.encode('{"command":["get_property","duration"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	duration = hdata(data["data"])

	sock.sendall(str.encode('{"command":["get_property","video-format"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	vformat = data["data"]

	sock.sendall(str.encode('{"command":["get_property","video-codec"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	vcodec = data["data"]

	sock.sendall(str.encode('{"command":["get_property","file-format"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	fformat = data["data"]

	sock.sendall(str.encode('{"command":["get_property","width"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	resx = data["data"]

	sock.sendall(str.encode('{"command":["get_property","height"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	resy = data["data"]

	sock.sendall(str.encode('{"command":["get_property","file-size"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	size = data["data"]

	sock.sendall(str.encode('{"command":["get_property","mpv-version"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	version = data["data"]

	msg = "{} [ {} |{}| {}/{} | {} | {}x{} | {} ]".format(version,
														  filename,
														  pbar(percent),
														  datetime.timedelta(seconds=float(timepos)),
														  datetime.timedelta(seconds=float(duration)),
														  fsize(size),
														  resx,
														  resy,
														  vformat)

	return msg

# mostrar informação
def mpv_np(world, world_eol, userdata):
	global sock
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

	try:
		sock.connect(MPVSOCK)
		conn = True
	except:

		conn = False

	if conn == True:
		w.command(w.current_buffer(), getInfos())
		sock.close()
	else:
		w.prnt(w.current_buffer(), "mpv não está sendo executado!")

	return w.WEECHAT_RC_OK

# Registro do Script
w.register(SCRIPT_NAME,
		   SCRIPT_AUTHOR,
		   SCRIPT_VERSION,
		   SCRIPT_LICENSE,
		   SCRIPT_DESC,
		   ' ', ' ')

# Comando
w.hook_command("mpv", "Now Playing", "", "/mpv", "", "mpv_np", "")
