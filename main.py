import librosa
import librosa.display
from colorama import Fore,Back,Style,init
import getpass
import matplotlib.pyplot as plt
from glob import glob
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def calcular_espectro(persona_copia,numero_copia,direccion_copia):
  data_dir = direccion_copia
  audio_files = glob(data_dir + '/*.mp3')
  len(audio_files)
  audio,sfreq = librosa.load(audio_files[numero_copia])
  X = librosa.stft(audio)
  Xdb = librosa.amplitude_to_db(abs(X))
  plt.figure(figsize=(14, 5))
  #Inserte titulo
  plt.title(f"Espectograma de frecuencias de la persona {persona_copia}")
  librosa.display.specshow(Xdb,sr=22050, x_axis='time', y_axis='hz')
  plt.show()
  

def run():
  init()
  username = getpass.getuser()
  uno = Fore.YELLOW + Style.BRIGHT + "(1)"
  dos = Fore.YELLOW + Style.BRIGHT + "(2)"
  print(Fore.GREEN + Style.BRIGHT + 
  f"""
Bienvenido {username}!
Elige una opcion del menu

{uno} Calcular los Hz   
{dos} Salir """)
  menu = int(input(Fore.BLUE + "Opcion:"+Style.RESET_ALL+ Fore.LIGHTWHITE_EX + ""))
  
  if menu == 1:
    clear()
    print(Fore.WHITE + Style.BRIGHT+"Escribe la cantidad de calculos a realizar:")
    cantidad = int(input(Fore.BLUE + "Cantidad:"+Style.RESET_ALL+ Fore.LIGHTWHITE_EX + ""))
    clear()
    print(Fore.WHITE + Style.BRIGHT+"Ubicacion de los audios (.mp3) [Ejemplo: users/documents/audio]")
    direccion = input(Fore.BLUE + "Ubicacion: "+Style.RESET_ALL+ Fore.LIGHTWHITE_EX + "")
    
    for i in range(cantidad):
      clear()
      print(Fore.WHITE + Style.BRIGHT+ f"Escribe el nombre de la persona #{i+1}:")
      persona = input(Fore.BLUE + "Nombre de la persona:"+Style.RESET_ALL+ Fore.LIGHTWHITE_EX + "")
      calcular_espectro(persona,i,direccion)
      
    print(Fore.RED + f"Hasta pronto {username}")
    sleep(3)
    clear()

  elif menu == 2:
    clear()
    print(Fore.RED + f"Hasta pronto {username}")
    sleep(3)
    clear()
    quit()                            

if __name__ == '__main__':
    run()