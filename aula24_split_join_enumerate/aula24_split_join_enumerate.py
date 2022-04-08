'''
AULA24 - SPLIT, JOIN & ENUMERATE
06- 07 / 04/22

 * SPLIT - divite uma string - str
 * JOIN - junta uma lista - str
 * ENUMERATE -  enumera elementos de uma lista # list /para objetos iteraveis
'''

# SPLIT

# str = 'O brasil é o pais do futebol, o brasil é penta'
# lista = str.split(' ')
# lista2= str.split(',')
# # print(lista2)
#
# # palavra = ''
# # contagem = 0
# for valor in lista2:
#     print(valor.strip().capitalize())
    # print(f'A palavra {valor} apareceu {lista.count(valor)} X na frase.')
    # qtd_vezes = lista2.count(valor)
    #
    # if qtd_vezes > contagem:
    #     contagem = qtd_vezes
    #     palavra = valor

# print(f'A palavra q apareceu mais vezes é {palavra} ({contagem}X)')

#JOIN

# str = 'O brasil é penta'
# lista1 = str.split(' ')
# str2 = ','.join(lista1)
#
# print(str)
# print(lista1)
# print(str2)

#ENUMERATE

# str = 'O brasil é penta'
# lista1 = str.split(' ')
#
# for indice, valor in enumerate(lista1):
#     print(indice, valor, lista1[indice])

lista = [
    [1,'mateus'],
    [3,'ceni'],
    [5,'balder'],
]
for indice, nome in lista:
    print(indice, nome)