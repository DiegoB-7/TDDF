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
  audio_files = glob(data_dir + '/*.wav')
  audio,sfreq = librosa.load(audio_files[numero_copia])
  X = librosa.stft(audio)
  Xdb = librosa.amplitude_to_db(abs(X))
  plt.figure(figsize=(14, 5))
  plt.title(f"Espectograma de frecuencias de la persona {persona_copia}")
  librosa.display.specshow(Xdb,sr=22050, x_axis='time', y_axis='hz')
  plt.show()
  

def run():
  init()
  system("title " + "TDDF")
  username = getpass.getuser()
  print(Fore.WHITE + Style.BRIGHT + f"""Bienvenido {username}!
Elige una opcion del menu para comenzar

(1) Calcular los Hz   
(2) Salir """ + "\n")
  print(Fore.BLUE + "Opcion:") 
  menu = int(input(""))
  
  if menu == 1:
    clear()
    print(Fore.WHITE + Style.BRIGHT+"Escribe la cantidad de calculos a realizar" + "\n")
    print(Fore.BLUE + "Cantidad:"+Style.RESET_ALL+ Fore.LIGHTWHITE_EX )
    cantidad = int(input(""))
    clear()
    print(Fore.WHITE + Style.BRIGHT+"Ubicacion de los audios (.wav) [Ejemplo: users/documents/audio]" + "\n")
    print(Fore.BLUE + "Ubicacion: "+Style.RESET_ALL+ Fore.LIGHTWHITE_EX )
    direccion = input("")
    
    for i in range(cantidad):
      clear()
      print(Fore.WHITE + Style.BRIGHT+ f"Escribe el nombre de la persona #{i+1}:" + "\n")
      print(Fore.BLUE + "Nombre de la persona:"+Style.RESET_ALL+ Fore.LIGHTWHITE_EX )
      persona = input("")
      calcular_espectro(persona,i,direccion)
    clear()  
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
