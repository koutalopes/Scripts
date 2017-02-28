import socket
import json
import datetime
import subprocess

MPVSOCK = "/tmp/mpvsocket"

def sConnect():
	global sock
	global conn
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

	try:
		sock.connect(MPVSOCK)
		conn = True
	except:
		conn = False

sConnect()

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

# def fsize(path):
# 	cmd = "mediainfo"
# 	args = "--Output=General;%FileSize/String%"
# 	s = subprocess.check_output([cmd, args, path]).decode("UTF-8")
#
# 	if s.split()[1] == "GiB":
# 		size = s.split()[0] + " Gb"
# 	elif s.split()[1] == "MiB":
# 		size = s.split()[0] + " Mb"
# 	else:
# 		size = s
#
# 	return size

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

	sock.sendall(str.encode('{"command":["get_property","path"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	path = data["data"]

	sock.sendall(str.encode('{"command":["get_property","mpv-version"]}\n'))
	data = json.loads(bytes.decode(sock.recv(1024)))
	version = data["data"]

	msg = "is playing {} ({}/{}) [{}] on mpv {}".format(filename,
														datetime.timedelta(seconds=float(timepos)),
														datetime.timedelta(seconds=float(duration)),
														vcodec,
														version)
	print(msg)

def showMsg():
	if conn == True:
		getInfos()
	else:
		print("Tem coisa errada ae noobão")

showMsg()