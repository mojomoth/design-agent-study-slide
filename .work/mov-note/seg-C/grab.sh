#!/bin/zsh
for t in "$@"; do /opt/homebrew/bin/ffmpeg -v error -y -ss $t -i "/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov" -frames:v 1 /Users/jeongyounglee/work/study/webdesign-agent-slide/.work/mov-note/seg-C/nat/t$t.png; done
