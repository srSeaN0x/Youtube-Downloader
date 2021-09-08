import pytube; import os; from moviepy.editor import *; from colorama import Fore

try:
  os.system('clear') # caso seu OS não seja windows e tenha dado erro mude para "cls" 
  url = str(input(Fore.MAGENTA + 'Digite a URL do vídeo: '))
  yt = pytube.YouTube(url)
  formato = str(input(Fore.MAGENTA + 'Deseja baixar o vídeo no formato MP3 ou MP4?: ')).upper()

  if formato == 'MP4':
    video = yt.streams.get_highest_resolution()
    download = video.download()
    print(f'\nVídeo "{yt.title}" baixado!')

  if formato == 'MP3':
    video = yt.streams.get_highest_resolution()
    download = video.download()
    join = os.path.join(download)
    clip = VideoFileClip(join)
    audio = clip.audio
    nome_novo = audio.write_audiofile(join + '.mp3')
    os.remove(f'{yt.title}.mp4')
    os.system('clear') # mesma coisa do primeiro comentário
    msg_sucesso = f'Áudio do vídeo "{yt.title}" baixado com sucesso.'
    print(Fore.BLACK + msg_sucesso)

except TypeError as erro:
  msg_erro = f'Houve um erro na entrada de dados. Tente novamente. (Erro: {erro})'
  print(Fore.RED + msg_erro)
