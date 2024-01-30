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

# importanto biblioteca
import os
import sys

operation_calc = {
    "operacao" : None,
    "n1": None,
    "n2": None
}

if len(sys.argv) > 1:

    # desempacotando o sys.argv:

    operacao, n1, n2 = sys.argv[1:]

    # Salvando os dados em suas respectivas variáveis:

    operation_calc['operacao'] = operacao.replace('--','').strip()
    operation_calc['n1'] = int(n1.replace('--','').strip())
    operation_calc['n2'] = int(n2.replace('--','').strip())


# Recebendo variáveis pelo input caso não seja usado o sys.argv:

if operation_calc['operacao'] is None:
    operacao = input("Qual operação deseja efetuar:").strip()
    n1 = int(input("Digite o primeiro número:").strip())
    n2 = int(input("Digite o segundo número:").strip())

    # indexando variáveis no dicionário:

    operation_calc['operacao'] = operacao
    operation_calc['n1'] = n1
    operation_calc['n2'] = n2

# declarando a função:
    
def calc (op, n1, n2):

    if op == "sum":
        result = n1 + n2
    elif op == "sub":
        result = n1 - n2
    elif op == "mul":
        result = n1 * n2
    else: 
        result = n1 / n2

    return result


            
        

# Inicio das operações
if __name__ == "__main__":

    resultado = calc(operation_calc['operacao'],operation_calc['n1'],operation_calc['n2'])
    
    # gravando logs:
    path = os.curdir
    filepath = os.path.join(path, "infixcalc.log")
    with open(filepath,"a") as file_:
        file_.write(f"{operation_calc['operacao']},{operation_calc['n1']},{operation_calc['n2']} = {resultado}\n")
    
    # Outra opção para a escrita : print(f"{operation_calc['operacao']},{operation_calc['n1']},{operation_calc['n2']} = {resultado}\n", file= open(filepath,"a"))     
    
    #Imprimindo o resultado da operação:
    print(f'O resultado operação {operation_calc["operacao"]} entre os números {operation_calc["n1"]} e {operation_calc["n2"]} é : {resultado}')
    


# Parei na aula #F22

# listas pastas no linux : ls
# criar pastas novas: mkdir nome-pasta
# criando pastas internas: mkdir pasta1/pastainterna
# descobrir o diretorio que estamos : pwd
# mudar de pasta: cd pasta
# mudanças alternativas: ls . ou cd . - ele lista o diretório atual ou muda para o direitorio atual
# mudanças alternativas : ls .. ou cd .. - lista diretórios anteriores ou muda para diretórios anteriores
# criar arquivos vázios em pastas : touch arquivo.txt
# gravar conteúdo nesses arquivos : echo "conteudo" >> pasta1/arquivo.txt
# lsitar o que esta na pasta1 e mostrar : cat pasta1/arquivo.txt
# apagar pasta: rm -rf pasta1 - sempre se certificar de que a pasta que você quer remover é exatamente essa
# sempre que for trabalhar com pastar, devemos utilizar o path, pois se mudar de SO não causar problemas
# path = os.path.join("pasta","subspasta")
# retornar o diretório atual : os.curdir - se for linux, retorna "." se for outro SO pode ser outro caracter
# criar um arquivo novo: os.mknod(os.path.join(path,"arquivo.txt"))
# filepath: filepath = os.path.join(path, "arquivo.txt")
# Retorna o nome do arquivo : os.path.basename(filepath)
# obter o caminho absoluto do arquivo : os.path.abspath(path)
# modo r: apenas leitura
# modo w: Escrita (apaga sempre que é aberto)
# modo a: append (adiciona as escritas)
# usando o contextmanengem: with opem)filepath, "a") as arquivo: # jeito certo de escrever em um arquivo
    #with é gerenciador de contexto
    #usamos isso pois ele abre e fecha o arquivo sozinho
# podemos usar o print para escrever dentro de um arquivo, dependendo do caso:
    # print("Brasil", file= open(filepath,"a"))


