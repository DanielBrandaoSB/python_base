"""Hello World Multi linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LAND devidamente configurada ex:

    export LAND =pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Daniel Brandão"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"




if __name__ == "__main__": # linha que define o bloco principal de python
    
    current_language = input("Qual linguagem você quer que apareça sua mensagem:")

    if current_language == "pt_BR":
        msg = "Olá, Mundo!"
    elif current_language == "it_IT":
        msg = "Cian, Mondo!"

    print(msg)
    
