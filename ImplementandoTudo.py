#! bin/usr/env python3
""" Recriando o bloco de notas

-- Teremos operações de escrita (NEW)
-- Teremos operações de leitura (TAG)

"""
__version__ = '0.0.1'
__author__ = 'Daniel Brandão'
__license__ = 'Unlisence'

import os
import sys
import logging
from logging import handlers
from datetime import datetime

# criando pasta de destino para anotações com OS:
path = os.curdir
filepath = os.path.join(path,'test.txt')

# Criando o template de logs:
log_level = os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.Logger("Daniel",log_level) # abrindo instância de log (stdout)
logf = logging.Logger("Daniel",log_level) # abrindo instância de log (gravação)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.setFormatter(fmt)
log.addHandler(ch)
# ------------------
fm = handlers.RotatingFileHandler(
    "MeuLogTest.log",
    maxBytes= 10**6,
    backupCount=10
)
fm.setLevel(log_level)
fm.setFormatter(fmt)
logf.addHandler(fm)

# estrutura de dados:
dados = {
    "log_level": None,
    "operacao": None,
    "tag": None,
    "text": None
}


if __name__ == "__main__":

    arguments = sys.argv[1:]

    try:
        operacao,tag,text = arguments
    except ValueError as e:
        log.error("você precisa passar todas as variáveis, tente : new --")
        logf.error("")
    

    


