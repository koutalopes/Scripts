#!/bin/bash

xrandr --output LVDS1 --mode 1366x768 --rate 60 --output HDMI1 --mode 1920x1080 --rate 60 --right-of LVDS1
synclient TouchpadOff=1
awesome-client 'awesome.restart()'
nitrogen --restore
xset s off
xset -dpms