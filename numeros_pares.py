#! usr/bin/python 3
"""
Faça um porgrama que impre os números pares de 1 a 200

ex
'python numeros_pares.py
'
2
4
6
8
...
"""

import sys
import os
from datetime import datetime

# Pegando os valores de data:
timestamp = datetime.now().isoformat()
# criando arquivo de salvamento para os dados realizados:
path = os.curdir
filepath = os.path.join(path,'Numeros_pares_impares.txt')

# obtendo argumentos por linha de comando:

# TODO: fazer uma melhoria para que seja escolhido se é impar ou par a operação

arguments = sys.argv[1:]

try:
    arguments = int(arguments[0])
except IndexError:
    arguments = input("Digite o número máximo de números:")
    arguments = int(arguments)

# mostrando os valores:    
for i in [n for n in range(0,arguments) if n % 2 == 0]: # for aninhado com list comprehesion
    print(i)

#Gravando dados:
with open(filepath,'a', encoding= 'UTF-8') as file_:
    file_.write(f"Número maximo de interações: {arguments} - {timestamp}\n")


