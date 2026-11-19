#!/bin/bash
# $1 = danh sách đoạn, $2 = file ra. Giải mã từng đoạn ra khung thô rồi mã hoá liền mạch 24 fps.
lst=$1; out=$2
( while read -r _ f; do f=${f//\'/}; ffmpeg -nostdin -v error -i "$f" -an -vsync passthrough -f rawvideo -pix_fmt yuv420p -s 1280x720 -; done < "$lst" ) | \
ffmpeg -v error -y -f rawvideo -pix_fmt yuv420p -s 1280x720 -r 24 -i - -c:v libx264 -preset veryfast -crf 17 -pix_fmt yuv420p -video_track_timescale 24000 "$out"
