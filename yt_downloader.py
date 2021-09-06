import pytube; import os; from moviepy.editor import *

url = str(input('Digite a URL do vídeo: '))
yt = pytube.YouTube(url)
formato = str(input('Deseja baixar o vídeo no formato MP3 ou MP4?: ')).upper()

if formato == 'MP4':
  video = yt.streams.get_highest_resolution()
  download = video.download()
  print(f'Vídeo "{yt.title}" baixado!')

if formato == 'MP3':
  video = yt.streams.get_highest_resolution()
  download = video.download()
  clip = VideoFileClip(download)
  audio = clip.audio
  audio.write_audiofile(download + '.mp3')
  path = os.path.abspath(download)
  diretorio = os.listdir(path)
  for file in diretorio:
      if file == f'{download}':
          os.remove(file)
