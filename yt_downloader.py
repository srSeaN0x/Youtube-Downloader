import pytube
import os
from moviepy.editor import *
from colorama import Fore, init
from time import sleep

init(autoreset = True)

try:
  while True:
    def clear():
      os.system('clear' if os.name != 'nt' else 'cls') 
    

    clear()
    url = str(input(Fore.MAGENTA + 'Digite a URL do vídeo: '))
    yt = pytube.YouTube(url)
    formato = str(input(Fore.MAGENTA + 'Deseja baixar o vídeo no formato MP3 ou MP4?: ')).strip().upper()

    if formato == 'MP4':
      video = yt.streams.get_highest_resolution()
      download = video.download()
      print(f'\nVídeo "{yt.title}" baixado!')
      sleep(3.3)
      clear()
      continue

    if formato == 'MP3':
      video = yt.streams.get_highest_resolution()
      download = video.download()
      join = os.path.join(download)
      clip = VideoFileClip(join)
      audio = clip.audio
      nome_novo = audio.write_audiofile(str(join).replace('mp4', 'mp3'))
      nome_arquivo = f'''{yt.title.replace("." if '.' in yt.title else "'", '')}.mp4'''
      os.remove(nome_arquivo)
      clear()
      msg_sucesso = f'Áudio do vídeo "{yt.title}" baixado com sucesso.'
      print(Fore.BLACK + msg_sucesso)
      sleep(3.3)
      clear()
      continue

    elif formato not in ('MP4', 'MP3'):
      MSG_ERRO = 'Você digitou algo errado, ou o programa não tem opções para esse formato.'
      print(Fore.RED + MSG_ERRO)
      sleep(4.4)
      clear()
      continue

except Exception as error:
  msg_erro = 'Houve um erro :(.'
  print(Fore.RED + msg_erro + ': ', error)
