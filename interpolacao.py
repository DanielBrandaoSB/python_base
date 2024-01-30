""" Interpolação

Descrição:

Script para validação dos conhecimentos em interpolação.
Com isso, foi desenvolvido um código para envio de emails
, com variáveis para serem anexada ao scritps

NAO MANDE SPAM!!!!

"""
__version__ = "0.1.1"
__author__ = "Daniel Brandão"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails e o texto de envio")
    sys.exit(1)
filename = arguments[0]
templatename = arguments[1]
path = os.curdir
filepath = os.path.join(path,filename) # emails.txt
templatepath = os.path.join(path,templatename) #email_temp.txt


clientes = []
for line in open(filepath):
   
   name, email = line.split(",")

    #clientes = ["Amanda", "Daniel", "Sofia","Alice", "Olivia"]
   
    # TODO: Substituir por envio de email
   print(f"Enviando email para:{email}")
   print()
   print(open(templatepath).read() % {
   "nome":name,
   "produto":"Caneta",
   "texto":"melhora a escrita",
   "quantidade": 10,
   "preco":50.99
    }
    
    )
   print("-" * 50)

    
 
 #paramos no vídeo #13 aos 30 minutos


 #Exemplo de formatação centralizada:

#print("{:^11}".format(name)) # o que tiver dentro das chaves será centralizado em 11 caracteres

#print("{:<11}".format(name)) # o que tiver dentro das chaves será jogado para esquerda 11 caracteres

#print("{:>11}".format(name)) # o que tiver dentro das chaves será jogado para direita 11 caaracteres

#print("{:-^11}".format(name)) # centraliza e preenche o restante com tracinhos


# parei no #F16