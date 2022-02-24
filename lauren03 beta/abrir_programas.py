import pyttsx3
import os
import pyautogui
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
   engine.setProperty('voice', voices [-3].id)
   engine = pyttsx3.init()
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate + 0.5)

def falar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()

def abrir_google():
   os.startfile(r"C:\Users\nataf\AppData\Local\Programs\Opera GX\launcher.exe")
   falar('abrindo o google')

def abrir_guia_anonima():
    os.startfile(r"C:\Users\nataf\AppData\Local\Programs\Opera GX\launcher.exe")
    sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'n')
    falar('abrindo a guia anonima')

def abrir_a_epic():
    os.startfile("C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")
    falar('abrindo a epic store')

def abrir_a_steam():
    os.startfile("C:\Program Files (x86)\Steam\Steam.exe")
    falar('abrindo a loja da steam')

def abrir_a_netflix():
    os.startfile("https://www.netflix.com/latest")
    falar('abrindo a netflix')

def abrir_o_booty_farm():
    os.startfile("https://www.nutaku.net/games/booty-farm/play/")
    falar('abrindo o booty farm')

def abrir_spotify():
    os.startfile('https://open.spotify.com/')
    falar('abrindo o spotify')

