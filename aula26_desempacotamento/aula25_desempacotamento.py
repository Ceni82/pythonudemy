'''
Desempacotamento de listas em Python - 08/04/22
'''

lista = ['mateus', 'balder', 'stefanie', 1,2,3,4,6,7,8,9]

# n1, n2, *outralista, numeros = lista
# *outralista, n1, n2, n3 = lista
n1, n2, *_ = lista
print(n1, n2)