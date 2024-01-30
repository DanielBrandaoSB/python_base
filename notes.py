#!/usr/bin/env python 3
""" Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text: 
Anotacao geral sobre carreira de tecnologia

$ notes.py read --tag = tech

...
...

"""
__version__ = "0.0.1"
__author__ = "Daniel Brandão"
__license__ = "Unlicense"

#Importando bibliotecas
import os
import sys
from datetime import datetime

#Armazenamento:
#anotacoes = {}

#Declarando path
path = os.curdir
filepath = os.path.join(path,'anotacoes.txt')

# colhendo os argumentos
arguments = sys.argv[1:]
if not arguments:
    print("Operação invalida, digite o tipo de operação e o seu respectivo titulo")
    print("Exemplo: notes.py operacao titulo")
    sys.exit(1)

cmds = ("read","new")
if arguments[0] not in cmds:
    print(f"Comandos inválidos {arguments[0]}")
    print("Digite algum dos comandos válidos: 'new', 'read'")
    sys.exit(1)


timestamp = datetime.now().isoformat()
if arguments[0].lower() == "new": 

    try:
         titulo = arguments[1] # TODO: Tratar exception
         text = [
            f"{titulo}",
            input("tag:").strip(),
            input("text:\n").strip(),
            f"data:{timestamp}"
         ]    
    except IndexError as e:
        print(f"[ERROR]: {str(e)}")
        print(f"Número de argumentos inválidos {arguments}")
        print("EX: notes.py new 'Minha Nota'/ notes.py read --tag = tech ")
        sys.exit(1)

    with open(filepath,"a", encoding= "UTF-8") as file_:
        file_.write("\t".join(text) + "\n")
        

else:
    operacao,tag = arguments
    head,body = tag.rsplit("=")
    for line in open(filepath).readlines():
        titulo, tag, texto, data = line.split("\t")
        if tag.lower() == body.lower():
            print("-"*20)
            print(f"Título:{titulo}")
            print(f"Tag:{tag}")
            print(f"Texto:{texto}")
            print(f"{data}")
            print("-"*20)


# Parei no vídeo #F28 em 47:33 min