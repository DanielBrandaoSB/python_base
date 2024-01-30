"""Calculadora Infix

Funcionamento : [Operação] [n1] [n2]

Operações:

sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ infixcalc.py --sum --5 --2
7

$ infixcalc.py --mul --10 --5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
resultado: 9
"""
__version__ = '0.1.0'
__author__ = 'Daniel Brandão'
__license__ = 'Unlicense'

import os
import sys
from datetime import datetime



while True:
    arguments = sys.argv[1:]

    if not arguments:
        operation = input("operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation,n1,n2]
    elif len(arguments) != 3:
        print("Número de arguments inválidos")
        print("ex: 'sum 5 5'")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum","sub","mul","div")
    if operation not in valid_operations:
        print("Operção inválida")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        # TODO: Repetição while + exceptions
        if not num.replace(".","").isdigit():
            print(f"Número inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
            validated_nums.append(num)
    try:
        n1,n2 = validated_nums
    except ValueError as e:
        print(f"[ERROR]:{str(e)}")
        print(f"Números de argumentos inválidos: {validated_nums}")
        print(print("ex: 'sum 5 5'"))
        sys.exit(1)

    # TODO: Usar dict de funções

    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2
    elif operation == "div":
        result = n1 / n2


    print(f"O resultado é {result}")


    # Gravando logs:
    timestamp = datetime.now().isoformat()
    user = os.environ.get("USERNAME")

    path = os.curdir
    filepath = os.path.join(path,"infixcalc2.log")

    try:
        with open(filepath,"a") as file_:
            file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
    except PermissionError as e:
        print(f"[ERROR]: {str(e)}")
        sys.exit(1)

    # Opção alternativa para escrita: print("f"{operation},{n1},{n2} = {result}\n""), file= open(filename,"a"))

    # Imprimindo os resultados da operação:

    cont = input("Deseja continuar com novas operações ?[y/n]").strip().lower()
    if cont != 'y':
        break

