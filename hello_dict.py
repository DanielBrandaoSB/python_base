"""Hello World Multi linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LAND devidamente configurada ex:

    export LAND =pt_BR

Ou informe atraves do CLE arguments '--lang'

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Daniel Brandão"
__license__ = "Unlicense"

import os 
import sys
import logging

# -----------------------------------------
log_level = os.getenv("LOG_LEVEL","WARNING").upper() # set o nível de log que podemos vê 
log = logging.Logger("Daniel",log_level) # Estou setando que minha instancia de debug é 10
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)
# ------------------------------------------


arguments = {
    "lang": None,
    "count": 1
}

remove = []


for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging
        log.error(
            "You need to use '=', you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
    key = key.replace('--','')
    #Key = key.lstrip("-").strip()
    value = value.strip()
    key = key.replace('--','')
    
    if key not in arguments:
        print(f'invalid option {key}')
        remove.append(key)
    #key = arg.split("=")[0].replace('--','')
    #value = arg.split("=")[1]
    arguments[key]= value

#removendo elementos não aceitos:

if len(remove) > 0:  
    for rev in remove:
        arguments.pop(rev)

# Define a current_language proveniente dos cli args
    
current_language = arguments['lang']


# Define a current_laguage proveniente das variáveis de ambiente 
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
     
    else: 
        current_language = input(
             "Choose a language:"
        )

current_language = current_language[:5]

if __name__ == "__main__": # linha que define o bloco principal de python

    linguagens = {'pt_BR': 'Olá, Mundo!',
                  'it_IT': 'Cian, Mondo!',
                  'en_US': 'Hello , World!',
                  'es_SP': 'Hola, Mundo!',
                  'fr_FR': 'Bonjour, Monde!'}
    
    #current_language = input("Qual linguagem você quer que apareça sua mensagem:").strip()
#
    #if current_language in linguagens:
    #    print(linguagens[current_language])
    #else:
    #    print("A linguagens solicitada não esta disponível")

    try:

        message = linguagens[current_language]
    except KeyError as e:
        print(f"[ERROR] {str(e)}")
        print(f"a chave que você passou não existe na opção de linguagem")
        print(f"Selecione alguma das opções a seguir: {list(linguagens.keys())}")
        sys.exit(1)

    print(message * int(arguments["count"]))


"""
# CRIANDO UMA VENV

python3 -m venv (nome da venv)

# ATIVANDO A VENV

(nome da venv)\Scripts\activate

"""


# Estou na aula #F21 do curso

# Parei na aula #F24 - 1:04hrs

