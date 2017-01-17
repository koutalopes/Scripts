#!/bin/bash
tname=$1
curl -u o.4jvAbyzSyO8OeLPhGbIJ1BHk9dRkIemm: https://api.pushbullet.com/v2/pushes -d type=note -d title="$tname downloaded!!"
notify-send rtorrent "$tname downloaded!!"
