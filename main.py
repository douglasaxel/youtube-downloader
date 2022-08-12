from pytube import YouTube
from pytube.cli import on_progress
from pathlib import Path
from slugify import slugify
from sys import argv

link = argv[1] if len(argv) >= 2 else ''
while link == '':
  link = input('URL do video: ')

outputDir = Path(
    argv[2] if len(argv) >= 3 else None
    or input('Pasta para salvar: ')
    or '/mnt/f/Videos/yt_downloader/'
)
yt = YouTube(link, on_progress_callback=on_progress)
name = f'{slugify(yt.title)}.mp4'

print(f'\nBaixando: {name}')
print(f'na pasta: {outputDir}')

ys = yt.streams.get_highest_resolution()

try:
  ys.download(outputDir, filename=name)
except:
  print('O video não está disponível para download.')
