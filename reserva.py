#!usr/bin/python 3

"""
Faça um programa de terminal que exibe ao usuário uma listas de quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponivel em um arquivo de texto separado por vírgula

'quartos.txt'
#codigo,nome,preço
1,Suite Master,500
2, Quarto Familia,200
3, Quarto Single,100
4, Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago

O programa deve salvar esta escolha em outro arquivo contendo as reservas

'reservas.txt'
# Cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve ecibir uma
mensahem informando que já está reservado.
"""

__version__ = '0.0.1'
__author__ = 'Daniel Brandão'
__license__ = 'unlicense'


# Importando Bibliotecas:

import os 
import sys


# Criando caminhos de arquivo:

path = os.curdir
filepath = os.path.join(path,'reservas.txt')  # local de gravação das reservas


if __name__ == '__main__':


    print('*'*10,'Seja Bem vindo ao hotel bom sossego'.upper(),'*'*10)
    print("*"*57,'\n')
    print('Escolha Seu Quarto:')

    #TODO: Tratar com Except
    for lines in open('quartos.txt','r'):
        codigo,quarto,preco = lines.split(',')
        print(f'{codigo} - {quarto} - R$ {preco} Reais/Diária\n')


    # Estrair informações dos inputs
    nome = input('Digite seu Nome:')
    num = int(input('Digite o número do quarto que deseja:'))
    qnt = int(input('Digite a quantidade de dias que deseja se hospedar:'))

    # Validar disponilidade do quarto:

    flag = True
    while flag:

        quarto_reservados = []
        if os.path.exists(filepath) == False:

            with open(filepath,'a', encoding= 'UTF-8') as file_:
                file_.write(f'{nome},{num},{qnt}\n')
        
            print(f'\n{nome.title()}, sua reserva por {qnt} dias ficará no valor de R${qnt} reais') 
            break  
 
        else:

            for line in open(filepath).readlines():
                
                nome,num,qnt = line.split(',')
                quarto_reservados.append(num)
                print(quarto_reservados)


            if len(quarto_reservados) < 4:
                
                if codigo in quarto_reservados:
                    print(f'O Quarto número {num} já esta reservado.')
                    print("Por favor insira novamente seus dados e escolhe outro quarto")
                    flag = True

                else:
                    flag = False
                
            else:

                print("Infelizmente tods os quartos estão ocupados.")
                print("Tente novamente em outra data")

            
    print(f'{nome.title()}, sua reserva por {qnt} dias ficará no valor de R${qnt} reais')   
 

    with open(filepath,'a', encoding='UTF-8') as file_:
        file_.write(f'{nome},{num},{qnt}\n')


        
         

    



