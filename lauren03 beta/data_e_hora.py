import datetime

from datetime import date

import pyttsx3


# bagulho de voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
   engine.setProperty('voice', voices[-1].id)
   engine = pyttsx3.init()
   rate = engine.getProperty('rate')
   engine.setProperty('rate', rate + 1)

#bglh orientado em objeto
data = date.today()

ano = datetime.date.today().year

horas = datetime.datetime.now().hour

minutos = datetime.datetime.now().minute

segundos = datetime.datetime.now().second

dia = int(datetime.date.today().day)

mes = int(datetime.date.today().month)

dia_da_semana = int(datetime.date.today().isoweekday())










ontem = dia - 1

ontem_dia_da_semana = dia_da_semana - 1

if ontem_dia_da_semana == 1:
    ontem_por_extenso = 'segunda-feira'

elif ontem_dia_da_semana ==  2:
    ontem_por_extenso = 'terça-feira'

elif ontem_dia_da_semana == 3:
    ontem_por_extenso = 'quarta-feira'

elif ontem_dia_da_semana == 4:
    ontem_por_extenso = 'quinta-feira'

elif ontem_dia_da_semana == 5:
    ontem_por_extenso = 'sexta-feira'

elif ontem_dia_da_semana == 6:
    ontem_por_extenso = 'sábado'

elif ontem_dia_da_semana == 7:
    ontem_por_extenso = 'domingo'



amanha = dia + 1

amanha_dia_da_semana = dia_da_semana + 1

if amanha_dia_da_semana == 1:
    amanha_por_extenso = 'segunda-feira'

elif amanha_dia_da_semana ==  2:
    amanha_por_extenso = 'terça-feira'

elif amanha_dia_da_semana == 3:
    amanha_por_extenso = 'quarta-feira'

elif amanha_dia_da_semana == 4:
    amanha_por_extenso = 'quinta-feira'

elif amanha_dia_da_semana == 5:
    amanha_por_extenso = 'sexta-feira'

elif amanha_dia_da_semana == 6:
    amanha_por_extenso = 'sábado'

elif amanha_dia_da_semana == 7:
    amanha_por_extenso = 'domingo'








#mes passado

mes_passado = mes - 1

if mes_passado == 1:
   mes_passado_por_extenso = 'dezembro'

elif mes_passado == 2:
    mes_passado_por_extenso = 'feveireiro'

elif mes_passado == 3:
    mes_passado_por_extenso = 'março'

elif mes_passado == 4:
    mes_passado_por_extenso = "abril"

elif mes_passado == 5:
    mes_passado_por_extenso = 'maio'

elif mes_passado == 6:
    mes_passado_por_extenso = 'junho'

elif mes_passado == 7:
    mes_passado_por_extenso = 'julho'

elif mes_passado == 8:
    mes_passado_por_extenso = 'agosto'

elif mes_passado == 9:
    mes_passado_por_extenso = 'setembro'

elif mes_passado == 10:
    mes_passado_por_extenso = 'outubro'

elif mes_passado == 11:
    mes_passado_por_extenso = 'novembro'

elif mes_passado == 12:
    mes_passado_por_extenso = 'dezembro'








#mes que vem

mes_que_vem = mes + 1

if mes_que_vem == 1:
   mes_que_vem_por_extenso = 'janeiro'

elif mes_que_vem == 2:
    mes_que_vem_por_extenso = 'feveireiro'

elif mes_que_vem == 3:
    mes_que_vem_por_extenso = 'março'

elif mes_que_vem == 4:
    mes_que_vem_por_extenso = "abril"

elif mes_que_vem == 5:
    mes_que_vem_por_extenso = 'maio'

elif mes_que_vem == 6:
    mes_que_vem_por_extenso = 'junho'

elif mes_que_vem == 7:
    mes_que_vem_por_extenso = 'julho'

elif mes_que_vem == 8:
    mes_que_vem_por_extenso = 'agosto'

elif mes_que_vem == 9:
    mes_que_vem_por_extenso = 'setembro'

elif mes_que_vem == 10:
    mes_que_vem_por_extenso = 'outubro'

elif mes_que_vem == 11:
    mes_que_vem_por_extenso = 'novembro'

elif mes_que_vem == 12:
    mes_que_vem_por_extenso = 'janeiro'





# bagulho de mes

if mes == 1:
   mes_por_extenso = 'janeiro'

elif mes == 2:
    mes_por_extenso = 'feveireiro'

elif mes == 3:
    mes_por_extenso = 'março'

elif mes == 4:
    mes_por_extenso = "abril"

elif mes == 5:
    mes_por_extenso = 'maio'

elif mes == 6:
    mes_por_extenso = 'junho'

elif mes == 7:
    mes_por_extenso = 'julho'

elif mes == 8:
    mes_por_extenso = 'agosto'

elif mes == 9:
    mes_por_extenso = 'setembro'

elif mes == 10:
    mes_por_extenso = 'outubro'

elif mes == 11:
    mes_por_extenso = 'novembro'

elif mes == 12:
    mes_por_extenso = 'dezembro'








#bagulho de dia da semana



if dia_da_semana == 1:
    dia_da_semana_por_extenso = 'segunda-feira'

elif dia_da_semana ==  2:
    dia_da_semana_por_extenso = 'terça-feira'

elif dia_da_semana == 3:
    dia_da_semana_por_extenso = 'quarta-feira'

elif dia_da_semana == 4:
    dia_da_semana_por_extenso = 'quinta-feira'

elif dia_da_semana == 5:
    dia_da_semana_por_extenso = 'sexta-feira'

elif dia_da_semana == 6:
    dia_da_semana_por_extenso = 'sábado'

elif dia_da_semana == 7:
    dia_da_semana_por_extenso = 'domingo'

#comandos













def que_dia_é_hoje():
    texto_resposta = (f'hoje é {dia_da_semana_por_extenso} dia {dia} de {mes_por_extenso} ')
    print(texto_resposta)
    engine.say(texto_resposta)
    engine.runAndWait()


def que_dia_foi_ontem():
    texto_resposta = (f'ontem foi {ontem_por_extenso} dia {ontem} de {mes_por_extenso} ')
    print(texto_resposta)
    engine.say(texto_resposta)
    engine.runAndWait()


def que_dia_e_amanha():
    texto_resposta = (f'amanhã vai ser {amanha_por_extenso} dia {amanha} de {mes_por_extenso} ')
    print(texto_resposta)
    engine.say(texto_resposta)
    engine.runAndWait()


def qual_foi_o_mes_passado():
    texto_resposta = (f'o mes passado foi {mes_passado_por_extenso} ')
    print(texto_resposta)
    engine.say(texto_resposta)
    engine.runAndWait()


def qual_vai_ser_o_proximo_mes():
    texto_resposta = (f'o mes que vem é {mes_que_vem_por_extenso} ')
    print(texto_resposta)
    engine.say(texto_resposta)
    engine.runAndWait()


def que_horas_sao():
    texto_resposta = (f'são {horas}:{minutos}')
    print(texto_resposta)
    engine.say(texto_resposta)
    engine.runAndWait()


def em_que_mes_estamos():
    texto_resposta = (f'estamos em {mes_por_extenso}')
    print(texto_resposta)
    engine.say(texto_resposta)
    engine.runAndWait()


def em_que_anos_estamos():
    texto_resposta = (f"estamos no ano de {ano}")
    print(texto_resposta)
    engine.say(texto_resposta)
    engine.runAndWait()


def txt_de_relatorio():
    texto_de_relatorio = f'hoje é {dia_da_semana_por_extenso}, {dia} de {mes_por_extenso}, {horas}:{minutos}.'
    print(texto_de_relatorio)
    engine.say(texto_de_relatorio)
    engine.runAndWait()










def de_manha_tarde_noite_ou_madruga():
    if horas in (6, 7, 8, 9, 10, 11):
        print('bom dia!')
        engine.say('bom dia')
        engine.runAndWait()

    elif horas in (12, 13, 14, 15, 16, 17):
        print('boa tarde!')
        engine.say('boa tarde')
        engine.runAndWait()

    elif horas in (18, 19, 20, 21, 22, 23):
        print('boa noite!')
        engine.say('boa noite')
        engine.runAndWait()

    elif horas in (0, 2, 3, 4, 5):
        print('boa madrugada chefe')
        engine.say('boa madrugada')
        engine.runAndWait()
