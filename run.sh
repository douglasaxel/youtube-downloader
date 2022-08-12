#!/bin/bash

source $HOME/Workstation/Personal/yt_downloader/.venv/bin/activate
python $HOME/Workstation/Personal/yt_downloader/main.py $1 $2
deactivate
