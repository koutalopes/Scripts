#!/bin/bash

for a in *.flac; do
	f="${a[@]/%flac/mp3}"
	ffmpeg -i "$a" -codec:a libmp3lame -q:a 3 -map_metadata 0 -vsync 2 "$f"
done
