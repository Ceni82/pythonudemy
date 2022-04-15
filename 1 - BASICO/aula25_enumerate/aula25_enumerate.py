'''

ENUMERATE - 07/05/22 - Duvidas
'''



lista = [
       #0        #1        #2
    ['mateus', 'balder', 'ceni'], #0
    ['joss', 'carlos', 'pedro'], #1
    ['sapo', 'salete', 'debora'], #2
]

# print(lista[1][2])
#
# enumerada = list(enumerate(lista))
# print(enumerada[1][1][2])
'''
[
     0   1
    (0, ['mateus', 'balder', 'ceni']), 
    (1, ['joss', 'carlos', 'pedro']), 
    (2, ['sapo', 'salete', 'debora'])
]
'''

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    # print(valor_enumerado)
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2)