#!/usr/bin/ env python3

import os
import sys

if os.path.exists("names.txt"): #verifica se o arquivo existe (True/False)
    print("O arquivo existe")
    input("...")
    names = open("names.txt").readlines() # Estamos lendo um arquivo sem saber o que ele contem
else:
    print("[Error]: file names.txt not found.")
    sys.exit(1)
# LBYL - look before you leap ( Olhe antes de pular/continuar)

if len(names) >= 3:
    print(names[2])
else:
    print("[Eroor]:Missing name in the list")
    sys.exit(1)
