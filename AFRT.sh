#!/bin/bash
name=$1
alias=$2
tname=${name// /*}
sname=${name// /\\\\ }
echo 
echo "# $name"
echo schedule = $alias, 5, 5, \"load.start=/home/kouta/.config/rtorrent/watch/*$tname*.torrent,d.directory.set=\\\"/home/kouta/Downloads/Torrents/Animes/Current/$sname/\\\"\"
