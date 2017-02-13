#!/usr/bin/python3
#
#	IRC bot on python using
#	Kouta_Kun
#	11/02/2017
#	0.1
#

import socket
import ssl
import datetime
import time
import threading

# Setup
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sirc = ssl.wrap_socket(ircsock)

# Server
host = "irc.rizon.net"
port = 9999 # Secure connection

# Bot identity
CHANNEL = ["#flooders",
		  ]
NICK = "Nozomu"
PASS = "YAhsu4GWlHV7VlfG"

# Admin
adminname = ["Kouta_Kun",
			 "Rykrdo_Kun",
			]
exitcode = "!quitbot"
con = False

def connect():
	try:
		sirc.connect((host, port))
		sirc.send(bytes("USER {} {} {} {}\r\n".format(NICK, NICK, NICK, NICK), "UTF-8"))
		time.sleep(1)
		sirc.send(bytes("NICK {} \r\n".format(NICK), "UTF-8"))
		con = True
	except Exception as exc:
		print ("Erro {}".format(exc))
		con = False

def sendmsg(target, msg):
	sirc.send(bytes("PRIVMSG {} :{}\r\n".format(target, msg), "UTF-8"))

def pingme():
	threading.Timer(180.0, pingme).start()
	sirc.send(bytes("PING {} \r\n".format("irc.rizon.net"), "UTF-8"))
	print("[{}] - PING Server".format(datetime.datetime.now().strftime("%X")))

def main():

	while 1:
		ircmsg = sirc.recv(4096).decode("UTF-8")
		ircmsg = ircmsg.strip('\r\n')
		print("[{}] - {}".format(datetime.datetime.now().strftime("%X"), ircmsg))

		if ircmsg.find("PING") != -1:
			sirc.send(bytes("PONG {} \r\n".format(ircmsg.split() [1]), "UTF-8"))
			print("[{}] - PONG ".format(datetime.datetime.now().strftime("%X")))

		if ircmsg.find("End of /MOTD command.") != -1:
			for i in CHANNEL:
				sirc.send(bytes("JOIN {} \r\n".format(i), "UTF-8"))
				time.sleep(1)
				sendmsg("nickserv", "IDENTIFY {} \r\n".format(PASS))
				time.sleep(1)
				try:
					pingme()
				except Exception as error:
					print (error)

connect()
main()
