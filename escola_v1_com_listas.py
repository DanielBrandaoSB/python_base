#!/user/bin/emv python3
""" Exibe relatórp de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequenta cadas uma das
atividades.

"""
__version__ = '0.1.0'
__author__ = 'Daniel Brandão'

# Dados
sala1 = ["Erik","Maia","Gustavo","Manuel","Sofia","Joana"]
sala2 = ["Joao","Antonio","Carlos","Maria","Isolda"]

aula_ingles = ["Erik","Maia","Joana","Carlos","Antonio"]
aula_musica = ["Erik","Carlos","Maria"]
aula_danca = ["Gustavo","Sofia","Joana","Antonio"]

atividades = [("Inglês",aula_ingles),
              ("Música",aula_musica),
              ("Dança",aula_danca)
              ]
# Listar alunos em cada atividade por sala


for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 35)
    
    atividade_sala1 = []
    atividade_sala2 = []
    
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    
    print("sala1", atividade_sala1)
    print("sala2", atividade_sala2)
    print()
    print("#" * 35)


    # parei no vídeo #17

    # tuplas = (dado1,dado2)

    #unpacked = dado1, dado2 = tuplas