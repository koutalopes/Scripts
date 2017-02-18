# -*- coding: utf-8 -*-
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
from apiclient.discovery import build

# Setup
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sirc = ssl.wrap_socket(ircsock)
DEV_KEY = 'AIzaSyBQ4_mRJbwOuWS_Wu3nVM9SqVXs2t36hAI'
yt = build('youtube', 'v3', developerKey=DEV_KEY)

# Server
host = "irc.rizon.net"
port = 9999 # Secure connection

# Bot identity
CHANNEL = ["#flooders",
		   "#testes",
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
		sirc.send(bytes("USER {} {} {} {}\r\n".format(NICK,
													  NICK,
													  NICK,
													  NICK), "UTF-8"))
		time.sleep(1)
		sirc.send(bytes("NICK {} \r\n".format(NICK), "UTF-8"))
		con = True
	except Exception as exc:
		print ("Erro {}".format(exc))
		con = False

def sendmsg(target, msg):
	sirc.send(bytes("PRIVMSG {} :{}\r\n".format(target,
												msg), "UTF-8"))

def pingme():
	threading.Timer(180.0, pingme).start()
	sirc.send(bytes("PING {} \r\n".format("irc.rizon.net"), "UTF-8"))
	print("[{}] - PING Server".format(datetime.datetime.now().strftime("%X")))

def youtube(vid):
	results = yt.videos().list(id=vid, part="id, snippet, statistics, contentDetails").execute()
	for result in results.get('items', []):
		title = result["snippet"]["title"]
		dur = result["contentDetails"]["duration"].split("PT")[1].lower()
		views = int(result["statistics"]["viewCount"])
		likes = int(result["statistics"]["likeCount"])
		dislikes = int(result["statistics"]["dislikeCount"])
		channel = result["snippet"]["channelTitle"]

		ytmsg = "{} ({}) | {:,}+ / {:,}- | views {:,} | {}".format(title,
																   dur,
																   likes,
																   dislikes,
																   views,
																   channel)
		return ytmsg

def main():

	while 1:
		ircmsg = sirc.recv(4096).decode("UTF-8")
		ircmsg = ircmsg.strip('\r\n')
		print("[{}] - {}".format(datetime.datetime.now().strftime("%X"),
								 ircmsg))

		if ircmsg.find("PING") != -1:
			sirc.send(bytes("PONG {} \r\n".format(ircmsg.split() [1]), "UTF-8"))
			print("[{}] - PONG ".format(datetime.datetime.now().strftime("%X")))

		if ircmsg.find("End of /MOTD command.") != -1:
			sendmsg("nickserv", "IDENTIFY {} \r\n".format(PASS))
			time.sleep(1)
			try:
				pingme()
			except Exception as error:
				print (error)
				
			for i in CHANNEL:
				sirc.send(bytes("JOIN {} \r\n".format(i), "UTF-8"))

		if ircmsg.find("PRIVMSG") != -1:
			nick = ircmsg.split('!', 1)[0][:1]
			msg = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]
			chan = ircmsg.split(' ')[2]

			if msg.find("youtube.com/") != -1:
				vid = msg.split('v=')[1][:11]
				ytmsg = youtube(vid)
				sendmsg(chan, ytmsg)

			if msg.find("youtu.be/") != -1:
				vid = msg.split("//")[1].split("/")[1][:11]
				ytmsg = youtube(vid)
				sendmsg(chan, ytmsg)

connect()
main()
