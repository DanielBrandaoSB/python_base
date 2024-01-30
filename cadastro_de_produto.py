#!/usr/bin/env python3

"""Cadastro de produto


"""
__version__ = '0.1.0'

import pprint
produto = {
     "nome":"caneta",
     "cor":["azul","branco"],
     "preco":3.23,
     "dimensao": {
            "altura":12.1,
            "largura":0.8
     },
     "em_estoque":True,
     "codigo":"45678",
     "codebar":None
}


cliente = {
    "nome":"Daniel"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}


total_compra = compra["quantidade"] * produto["preco"]

print(
    f"O cliente {compra['cliente']['nome'] } comprou {compra['produto']['nome']} {compra['produto']['cor'][1]} "
    f" e pagou o total de {total_compra}."
)

#parei no minuto 33:12 do vídeo #F18 - Dicionário