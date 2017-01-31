#!/usr/bin/python3
#
#	IRC bot on python
#	Kouta_Kun
#	29/01/17
#	0.1
#

import socket
import ssl
import datetime
import time

sirc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sirc = ssl.wrap_socket(ircsock)

server = "irc.rizon.net"
port = 6667 # Secure connection
channel = "#flooders"
botnick = "kBot"
adminname = "Kouta_Kun"
exitcode = "!quitbot"
con = False

def connect():
	try:
		sirc.connect((server, port))
		sirc.send(bytes("USER {} {} {} Python Bot Test\n".format(botnick, botnick, botnick), "UTF-8"))
		sirc.send(bytes("NICK {}\n".format(botnick), "UTF-8"))
		con = True
	except Exception:
		con = False

def pong(ping):
	pingn = ping.split()[1]
	sirc.send(bytes("PONG {}\r\n".format(pingn), "UTF-8"))
	print ("PONG {}".format(pingn))

def sendmsg(msg, target=channel):
	sirc.send(bytes("PRIVMSG {} :{}\n".format(target, msg), "UTF-8"))

def main():
	while 1:
		ircmsg = sirc.recv(2048).decode("UTF-8")
		ircmsg = ircmsg.strip('\n\r')
		st = str(datetime.datetime.now()).split('.')[0]
		print ('[{}] {}'.format(st, ircmsg))

		if ircmsg.find("End of /MOTD command.") != -1:
			sirc.send(bytes("JOIN {}\n".format(channel), "UTF-8"))

		if ircmsg.find("PRIVMSG") != -1:
			nick = ircmsg.split('!',1)[0][1:]
			msg = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
			alvo = ircmsg.split()[2]

			# admin commands
			if nick.lower() == adminname.lower():
				if msg.rstrip() == exitcode:
					sendmsg("\o\~~~", alvo)
					sirc.send(bytes("QUIT \n", "UTF-8"))
					return

				if msg.split()[0] == "!join":
					sirc.send(bytes("JOIN {}\n".format(msg.split()[1]), "UTF-8"))
					print("JOIN {}".format(msg.split()[1]))

		else:
			if ircmsg.find("PING :") != -1:
				time.sleep(2)
				pong(ircmsg)

connect()
main()
