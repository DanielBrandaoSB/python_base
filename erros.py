#!/usr/bin/ env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    raise RuntimeError("Ocorreu um error") # usamos o Raise para forçar um error
except Exception as e:
    print(str(e))

try: #verifica se o arquivo existe (True/False)
    names = open("names.txt").readlines() # tenta abrir o arquivo, se não existir vai para a except # FileNotFoundError
    1 / 1 #ZeroDivisionError
    print(names.append) # AttributeError
except FileNotFoundError as e: # Bare except
    print(f"{str(e)}")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error]: You cant divide by zero")
    sys.exit(1)
except AttributeError:
    print("[Error]: List doesn't have banana")
    # TODO: Usar retry
else:
    print("Sucesso!!!") # Se o Try funcionar, ele é executado
finally:
    print("Execute isso sempre!!!") # Sempre é executado, mesmo com o try dando error

try:
    print(names[2]) # imprime o dado de index 2, se não existir vai para o except
except:
    print("[Eroor]:Missing name in the list")
    sys.exit(1)


#Parei na aula #F24 no minuto 48:59 min