#!/bin/bash
tname=$1
curl -u o.xwcYzAMLjd7aj8tUvGPH5pXefqFl7TRE: https://api.pushbullet.com/v2/pushes -d type=note -d title="$tname downloaded!!"
notify-send rtorrent "$tname downloaded!!"
