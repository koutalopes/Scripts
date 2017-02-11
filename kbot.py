#!/usr/bin/python3
#
#	IRC bot on python using bottle + asyncio
#	Kouta_Kun
#	11/02/2017
#	0.1
#

import bottom
import asyncio

host = "irc.rizon.net"
port = 9999 # Secure connection
ssl = True

CHANNEL = "#flooders"
NICK = "Nozomu"
PASS = "YAhsu4GWlHV7VlfG"

adminname = "Kouta_Kun"
exitcode = "!quitbot"

bot = bottom.Client(host=host, port=port, ssl=ssl)

@bot.on('CLIENT_CONNECT')
async def connect(**kwargs):
	bot.send('NICK', nick=NICK)
	bot.send('USER', user=NICK,
					 realname='botton + asyncio irc bot')
	bot.send('PASS', password=PASS)

	# Não tentar entrar em nenhum canal até o fim do MOTD
	done, pending = await asyncio.wait(
		[bot.wait("RPL_ENDOFMOTD"),
		 bot.wait("ERR_NOMOTD")],
		loop=bot.loop,
		return_when=asyncio.FIRST_COMPLETED
	)

	for future in pending:
		future.cancel()

	bot.send('JOIN', channel=CHANNEL)

@bot.on('PING')
def keepalive(message, **kwargs):
	bot.send('PONG', message=message)

bot.loop.create_task(bot.connect())

bot.loop.run_forever()
