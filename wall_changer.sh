#!/bin/bash
arq=$(shuf -n 1 'caminho para o aquivo com a lista' | sed 's/ /\%20/g')

gsettings set org.gnome.desktop.background picture-uri file:///'caminho para a pasta de wallpapers'/$arq
gsettings set org.gnome.desktop.background picture-options 'scaled'
gsettings set org.gnome.desktop.background primary-color '#716b6b'
gsettings set org.gnome.desktop.background secondary-color '#7d7e4f'
gsettings set org.gnome.desktop.background color-shading-type 'vertical'
