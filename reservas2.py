import sys
import logging


ocupados = {}
try:
    for line in open('reservas2.txt'):
        nome,codigo,dias = line.strip().split(",")
        ocupados[int(codigo)]= {
            "nome": nome,
            "dias": dias
                      }
except FileNotFoundError:
    logging.error("arquivo Reservas2.txt não existe")
    sys.exit(1)


quartos = {}
try:
    for line in open('quartos.txt'):
        codigo,nome,preco = line.strip().split(",")
        quartos[int(codigo)]= {
            "nome": nome,
            "preco": float(preco),# TODO: Decimal
            'disponivel': False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("arquivo Quartos.txt não existe")
    sys.exit(1)



print("Reserva Hotel Bom Sossego")
print("-"*40)


if len(ocupados) == len(quartos):
    print("Hotel Lotado")
    sys.exit(1)


nome_c = input("Nome do cliente:").strip()
print("Lista de quarto")
for codigo, dados in quartos.items():
    #TODO: Substitiuir casa decimal por vírgula
    nome = dados['nome']
    preco = dados['preco']
    disponivel = 'ocupado' if not dados['disponivel'] else 'livre'
    print(f'{codigo} - {nome} - R${preco} Reais - {disponivel}')

print("-"*40)


try:
    num_quarto = int(input("Digite o número do quarto que deseja reservar:").strip())
    if not quartos[num_quarto]['disponivel']:
        print(f'O quarto {num_quarto} está ocupado')
        sys.exit(1)
 
except ValueError:
    logging.error("Número inválido, digite apenas números")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)


try:
    dias = int(input("Digite o número de dias de hospedagem:").strip())
except ValueError:
    logging.error("Numero inválido, digite apenas números")



custo = quartos[num_quarto]['preco'] * dias
print(f'{nome_c} você escolheu o quarto {quartos[num_quarto]["nome"]} e vao custar R$ {custo} Reais')


# Gravando Valores 
with open('reservas2.txt','a',encoding='UTF-8') as file_:
    file_.write(f'{nome_c},{num_quarto},{dias}\n')