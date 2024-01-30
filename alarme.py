#! usr/bin/python3
"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar
Sendo que caso será exibidade um mensagem de alerta dependendo das seguintes condições:

temp maior 45: Alerta!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: Alerta!!! period de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp < 0: Alerta: Frio extremo

"""

import pyowm as pw
import os 
import sys
from datetime import datetime


# Obtendo temperatura da API OpenWeath:

owm = pw.OWM(api_key='d989bfa8e1857b3fbc488ff2e4415cf8')
observation  = owm.weather_manager()
weath = observation.weather_at_place('Posse,BR').weather
temp = weath.temperature('celsius')

# criando caminho de gravação de alertas:
path = os.curdir
filepath = os.path.join(path,'alarme.txt')


# algoritmo:

if temp['temp'] > 45:
    print(f"Alerta!! Perigo de valor extremo, temperatura está {temp['temp']} graus celsius")
elif  30 <= temp['temp'] <= 45:
    print(f"A temperatura está alta, {temp['temp']} graus celsius")
elif  10 <= temp['temp'] <= 30:
    print(f"A temperatura está Normal, {temp['temp']} graus celsius")
elif 0 <= temp['temp'] <= 10:
    print(f" está frio, {temp['temp']} graus celsius")
else:
    print("Frio extremo")


# Salvando dados:
timestamp = datetime.now().isoformat()
with open(filepath,'a',encoding= 'UTF-8') as file_:
    file_.write(f"Temperatura: {temp['temp']} - {timestamp}\n")



