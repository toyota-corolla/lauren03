import pyautogui

import os

import data_e_hora as tempo

import abrir_programas as cf #aka comandos foda

import pyttsx3

from time import sleep

import spotify

import pyautogui as p

import lista_de_acionamento_de_comandos as l


#configs da sintese de voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
   engine.setProperty('voice', voices [-3].id)
   engine = pyttsx3.init()
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate + 10)

def falar(textinho):
   engine.say(textinho)
   engine.runAndWait()

#inicio do programa

tempo.de_manha_tarde_noite_ou_madruga()

tempo.txt_de_relatorio()


while True:
   pergunta = input('o que o senhor deseja?: ')

   if pergunta in l.hora:
      tempo.que_horas_sao()

   elif pergunta in l.dia:
      tempo.que_dia_é_hoje()

   elif pergunta in l.mes:
      tempo.em_que_mes_estamos()

   elif pergunta in l.ano:
      tempo.em_que_anos_estamos()

   elif pergunta in l.ontem:
      tempo.que_dia_foi_ontem()

   elif pergunta in l.amanha:
      tempo.que_dia_e_amanha()

   elif pergunta in l.mes_passado:
      tempo.qual_foi_o_mes_passado()

   elif pergunta in l.mes_que_vem:
      tempo.qual_vai_ser_o_proximo_mes()

   if pergunta in l.toca_um_som:
    spotify.toca_trap()

   elif pergunta in l.toca_um_som_br:
      spotify.toca_trapBR()

   elif pergunta in l.toca_um_funk:
      spotify.toca_funk()

   elif pergunta in l.pausar_musica_no_spotify:
      spotify.pausar_musica()



   elif pergunta in l.abre_o_google:
      cf.abrir_google()

   elif pergunta in l.abre_a_guia_anonima:
      cf.abrir_guia_anonima()

   elif pergunta in l.abre_a_epic:
      cf.abrir_a_epic()

   elif pergunta in l.abre_a_steam:
      cf.abrir_a_steam()

   elif  pergunta in l.abre_a_netflix:
    cf.abrir_a_netflix()

   elif pergunta in l.abre_o_booty_farm:
    cf.abrir_o_booty_farm()

   elif pergunta in l.abre_o_spotify:
      cf.abrir_spotify()




   if 'pesquise' in pergunta:
      termo_pesquisa = (pergunta[9:])
      os.startfile(f"https://www.google.com/search?q={termo_pesquisa}")
      texto = f'pesquisando {termo_pesquisa}'
      print(texto)
      falar(texto)

   if 'pesquisar' in pergunta:
      if 'na guia anonima' in pergunta:
         termo_pesquisa = (pergunta[9:-15])
         os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
         sleep(1)
         pyautogui.hotkey('ctrl', 'shift', 'n')
         sleep(1)
         pyautogui.write(termo_pesquisa)
         pyautogui.hotkey('enter')
         texto = f'pesquisando {termo_pesquisa} na guia anonima'
         falar(texto)

      elif "no youtube" in pergunta:
         termo_pesquisa = (pergunta[9:-10])
         os.startfile(f'https://www.youtube.com/results?search_query={termo_pesquisa}')
         texto = f'pesquisando {termo_pesquisa} no youtube'
         print(texto)
         falar(texto)

      elif 'imagens de' in pergunta:
         termo_pesquisa = (pergunta[21:])
         os.startfile(f'https://www.google.com.br/search?q={termo_pesquisa}&sxsrf=AOaemvLuc6mM5S_Z-BFe9B93JJKvII50MQ:1640915952446&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiUj86j-Iz1AhU3HrkGHYAODlkQ_AUoAXoECAEQAw&biw=1319&bih=624')
         falar(f'procurando imagens de {termo_pesquisa}')
      else:
            termo_pesquisa = (pergunta[10:])
            os.startfile(f"https://www.google.com/search?q={termo_pesquisa}")
            texto = f'pesquisando {termo_pesquisa}'
            print(texto)
            falar(texto)


   elif 'como' in pergunta:
      print('ok')
      como = (pergunta[:])
      os.startfile(f'https://www.google.com/search?q={como}')
      texto = f'procurando {como} na internet'
      print(texto)
      falar(texto)

   elif 'traduz' in pergunta:
      traduzir = (pergunta[7:])
      os.startfile(f'https://translate.google.com.br/?sl=auto&tl=pt&text={traduzir}')
      texto = f'procurando o significado de {traduzir} em portugues'
      print(texto)
      falar(texto)

   elif 'peito diz' in pergunta:
         if 'em ingles' in pergunta:
            a_bonekinha_nao_sabe_brincar = (pergunta[9:-10])
            os.startfile(f'https://translate.google.com.br/?sl=pt&tl=en&text={a_bonekinha_nao_sabe_brincar}')
            texto = f'procurando oque significa {a_bonekinha_nao_sabe_brincar} em ingles'
            print(texto)
            falar(texto)


   elif pergunta == 'posicao':
       a = p.position()
       print(a)

   if pergunta == 'qual seu nome?':
      print('como assim tu esqueceu meu nome filha da puta')
      falar(f'como assim tu esqueceu meu nome filha da puta?')

      print('vai se foder, otario')
      falar('vai se foder otario')
      break

   elif pergunta == 'sair':
      print('vlw meu mano, qualquer coisa tamo ai')
      falar('valeu meu mano, qualquer coisa tamo aí')
      break
