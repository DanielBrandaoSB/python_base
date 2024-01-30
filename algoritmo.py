""" # Algoritmos

Sequencia de instruções lógicas que visam obter a solução
de um problema.

## Fazer o mesmo algoritmo do vídeo #F26 com a API do tempo e Datetime
## Além de aplicar os outros conhecimentos aprendidos


"""
import pyowm as pw
from datetime import datetime


data,time = str(datetime.now()).split(" ")
weekday = datetime.now().isoweekday()
owm = pw.OWM(api_key='d989bfa8e1857b3fbc488ff2e4415cf8')

a = owm.weather_manager()

a.weather_around_coords()




print(a)
if data == '2024-01-16':
    print("ok")

#parei na aula de #F28