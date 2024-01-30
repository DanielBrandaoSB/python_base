#!/user/bin/emv python3
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequenta cadas uma das
atividades.

"""
__version__ = '0.1.1'
__author__ = 'Daniel Brandão'

# Dados

salas = {'sala1':["Erik","Maia","Gustavo","Manuel","Sofia","Joana"],
         'sala2':["Joao","Antonio","Carlos","Maria","Isolda"]}

#sala1 = ["Erik","Maia","Gustavo","Manuel","Sofia","Joana"]
#sala2 = ["Joao","Antonio","Carlos","Maria","Isolda"]

aulas = {'aula_ingles':["Erik","Maia","Joana","Carlos","Antonio"],
         'aula_musica':["Erik","Carlos","Maria"],
         'aula_danca':["Gustavo","Sofia","Joana","Antonio"]}

#aula_ingles = ["Erik","Maia","Joana","Carlos","Antonio"]
#aula_musica = ["Erik","Carlos","Maria"]
#aula_danca = ["Gustavo","Sofia","Joana","Antonio"]



# Listar alunos em cada atividade por sala


for nome_atividade, atividade in aulas.items():
   
   print(f"Alunos da atividade {nome_atividade}\n")
   print("-" * 35)
   
   atividade_sala1 = set(salas['sala1']) & set(atividade)
   atividade_sala2 = set(salas['sala2']).intersection(set(atividade))
   

   # sala1 que tem interseção com a atividade

   #for aluno in atividade:
   #    if aluno in sala1:
   #        atividade_sala1.append(aluno)
   #    elif aluno in sala2:
   #        atividade_sala2.append(aluno)
   
   
   print(nome_atividade, atividade_sala1)
   print(nome_atividade, atividade_sala2)
   print()
   print("#" * 35)


