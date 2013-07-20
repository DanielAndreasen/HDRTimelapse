#!/bin/bash

echo "Making the resized folder..."
mkdir resized
echo "Resizing..."
mogrify -path resized -resize 1920x1080! *.jpg
cd resized

ls -1tr | grep -v files.txt > files.txt

echo "Combining the photos..."
mencoder -nosound -noskip -oac copy -ovc copy -o output.avi -mf fps=15 'mf://@files.txt' 

echo "Compress to output-final.avi"
ffmpeg -i output.avi -y -s hd1080 -sameq output-final.avi
