# união

conjunto_a = [1,2,3,4,5]
conjunto_b = [4,5,6,7,8]

set(conjunto_a) | set(conjunto_b)
set(conjunto_a).union(set(conjunto_b))

# interseção

set(conjunto_a) & set(conjunto_b)
set(conjunto_a).intersection(conjunto_b)

# diferença

set(conjunto_a) - set(conjunto_b) # A ordem importa
set(conjunto_a).difference(set(conjunto_b))

# diferença simetrica

set(conjunto_a).symmetric_difference(set(conjunto_b)) # Nesse caso, pegaram os objetos que não estão nos 
                                                      # dois conjuntos. Ou seja, os diferetes.

set(conjunto_a) ^ set(conjunto_b)


# Os sets implementam Hash Table

numeros = [1,2,3,4,5,5,6,3,2,5,8,7]

3 in numeros 
# quando temos uma lista, o python tem que buscar dentro da lista e verificar
# sendo que a velocidade é O(n)

# quando colocamos em um set, temos apenas um número e isso facilita devido
# a hash table.


