#!/usr/bin/env python3

from logging import handlers
import logging
import os

# Template padrão de gravação de logs:

log_level = os.getenv("LOG_LEVEL",'WARNING').upper() # pego o level da variável de ambiente se não for passado nenhum nível

log = logging.Logger("Daniel",log_level) # nome vai ser Daniel com o nível configurado de log_level
ch = logging.StreamHandler()
ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "MeuLog.log"
    maxBytes= 10**6,
    backupCount= 10
)

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)

ch.setFormatter(fmt)
log.addHandler(ch)



# BOILERPLATE
# TODO: usar função
# TODO: usar lib(loguru)
log_level = os.getenv("LOG_LEVEL","WARNING").upper() # set o nível de log que podemos vê
# nossa instancia 
log = logging.Logger("Daniel",log_level) # Estou setando que minha instancia de debug é 10
# level
#ch = logging.StreamHandler()
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
     maxBytes= 10**6, # normalmente usado 10**6
     backupCount=10
)
# formatacao
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
# destino
#log.addHandler(ch)
log.addHandler(fh)


#log.debug("Mensagem pro dev, qe, sysadmin")
#log.info("Mensagem geral para usuários")
#log.warning("Aviso que não causa erro")
#log.error("Erro que afeta uma única execução")
#log.critical("Erro que afeta todo mundo Ex: O banco de dados sumiu")

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu error %s", str(e))


    #parei na aula #F26 (Refazer todo o conteúdo sozinho até logs)