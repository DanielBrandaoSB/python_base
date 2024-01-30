# quando a busca no dificionário se de pela chave, a velocidade será O(1), isto é, constante.
# Pois o dicionário utiliza a busca pela hash table

# quando a busca é pelo valor, já não é tão perfomático assim.

# Operações Dict:

cliente = {'nome':'Daniel', 'cod': 123} 
print(cliente)

#adicionando elementos:

cliente['cidade'] = 'Goiânia'
print(cliente)

#altera elementos existentes:

cliente["nome"] = "Daniel Brandão"
print(cliente)

# protocolo __contains__:

"nome" in cliente

#Retorna elementos:

print(cliente["nome"][0])

#Retorna elementos:

print(cliente["nome"][0:2].upper()) # retorna os 2 primeiro elementos do nome em maiúsculo

#Retorna elementos:

print(cliente['nome'][0:2].upper().replace('D','C').__add__("sa".upper())) # retorna os 2 primeiros elementos em maiúsculo 
                                              # e faz o replace logo em seguida do B pelo C

#Deletar elementos do dict:

del cliente['cidade']

print(cliente)

#tamanho do dict:

print(len(cliente))

#verificar keys:

print(cliente.keys())

#verificar itens:

print(cliente.items())

#adicionar dois dicionários:

país = {"país":'Brasil'}

print(f"dict1 = {cliente} e dict2 = {país}")

# juntando eles:

cliente.update(país)

print(cliente)


#Desenpacotando um dicionário:

#key,value = {**país}

#print(f"desempacotando o dicionario país: key: {key}, value:{value}")

# Desempacotando dois dicionários e formando um só:

final = {**cliente,**país}

print(final)


#desempacotamento de listas:
d = [1,2,3,4,5,6,8]
head,*body,tail = d

print(head)
print(body)
print(tail)

# nesse caso o desempacotamento é feito com o primeiro elemento em head
# o último elemento em tail e o restante aglomerado no body

# Desempacotamento de dict:

# como o dict tem dois valores, o key e o value, devemos colocar  duas **

variavel_final = {**cliente,**país}

print(f"Desse modo, teremos um dict único: {variavel_final}")