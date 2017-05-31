#!/bin/bash

save=$1

for a in *.flac; do
	f="${a[@]/%flac/mp3}"
	ffmpeg -i "$a" -codec:a libmp3lame -q:a 3 -map_metadata 0 -vf scale=500:500 -vsync 2 "$save/$f"
done
