"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras
e impreme cada uma das palavras com suas vogais duplicadas.

Ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python'
'Digite uma palavra (ou enter para sair):' Daniel'
'Digite uma palavra (ou enter para sair):' <enter>'
pythoon
Bruunoo
"""

import os
import sys
from datetime import datetime

# Armazenamento dos arquivos:
path = os.curdir
filepath = os.path.join(path,'palavra_duplicada.txt')

arquivo = []
vogais = ['a','e','i','o','u']
while True:
    palavra = input('Digite uma palavra (ou enter para sair):').strip()
    if not palavra:
        break

    palavra_dupli = ""
    for i in palavra:
        """if i.lower() in vogais:
            palavra_dupli += i * 2
        else:
            palavra_dupli += i
    """
    #IF ternário

        palavra_dupli += i * 2 if i.lower() in vogais else i


    arquivo.append(palavra_dupli)
    with open(filepath,'a',encoding= 'UTF-8') as file_:
        file_.write(f"{palavra} - {palavra_dupli}\n")

print(*arquivo,sep='\n')

    



# 52 min do #F29