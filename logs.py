#!/usr/bin/env python3

import logging
import os


# TODO: usar função
# TODO: usar lib(loguru)
log_level = os.getenv("LOG_LEVEL","WARNING").upper() # set o nível de log que podemos vê
# nossa instancia 
log = logging.Logger("Daniel",log_level) # Estou setando que minha instancia de debug é 10
# level
ch = logging.StreamHandler()
ch.setLevel(log_level)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)


log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro que afeta todo mundo Ex: O banco de dados sumiu")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("Deu error %s", str(e))