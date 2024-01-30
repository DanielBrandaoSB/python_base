#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10

---Tabuada do 1---
1
2
3
...
##################
---Tabuada do 2---
1
2
3
...

"""
__version__ = "0.1.1"
__author__ = "Daniel Brandão"



#base = [1,2,3,4,5,6,7,8,9,10]
base = list(range(1,11))       

# iterable (percorriveis)

for n1 in base:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in base:
        resultado = n1 * n2
        print("{:^18}".format(f'{n1} * {n2} = {resultado}'))
    
    print()
    print("#" * 18)
    









