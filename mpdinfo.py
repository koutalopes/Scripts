# -*- codinf: utf-8 -*-

from mpd import MPDClient
import subprocess

client = MPDClient()
client.connect("localhost", 6600)

info = client.currentsong()

arq = info['file']
artist = info['artist']
album = info['album']
title = info['title']
date = info['date']

subprocess.call(['mpc'])
