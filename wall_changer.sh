#!/bin/bash
arq=$(shuf -n 1 ~/Pictures/Wallpapers/list | sed 's/ /\%20/g')

gsettings set org.gnome.desktop.background picture-uri file:///home/kouta/Pictures/Wallpapers/$arq
gsettings set org.gnome.desktop.background picture-options 'scaled'
gsettings set org.gnome.desktop.background primary-color '#716b6b'
gsettings set org.gnome.desktop.background secondary-color '#7d7e4f'
gsettings set org.gnome.desktop.background color-shading-type 'vertical'
