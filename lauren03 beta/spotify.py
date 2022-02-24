import pyautogui
import os
from time import sleep
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
   engine.setProperty('voice', voices[-3].id)
   engine = pyttsx3.init()
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate + 0.5)



def toca_trap():
    os.startfile('https://open.spotify.com/playlist/3yy36Drf5C7XLXxhnzR5Z0')
    engine.say('tocando play list de trap')
    engine.runAndWait()
    sleep(10)
    pyautogui.click(x=342, y=463)

def toca_trapBR():
    os.startfile('https://open.spotify.com/playlist/0odICWw5cMt6WVOQypd0Eq')
    engine.say('tocando playlist de trap brasileiro')
    engine.runAndWait()
    sleep(10)
    pyautogui.click(x=342, y=463)

def toca_funk():
    os.startfile('https://open.spotify.com/playlist/0OxXWNFazide5Ym8DZlYpP')
    engine.say('tocando playlist de funk')
    engine.runAndWait()
    sleep(10)
    pyautogui.click(x=342, y=463)

def pausar_musica():
    os.startfile('https://open.spotify.com')
    sleep(7)
    pyautogui.click(x=699, y=641)
    pyautogui.hotkey('ctrl', 'w')
    engine.say('musica pausada')
    engine.runAndWait()