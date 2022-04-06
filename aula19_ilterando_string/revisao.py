'''


REVISAO- ITERANDO STRINGS COM WHILE-


# Indice
#       0123456789.......................33
frase = "O rato roeu a roura do rei de roma"
'''

frase = 'O rato roeu a roura do rei de roma'
tamanho_frase = len(frase)
# print(tamanho_frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    letra = frase [contador]
    if letra == 'r':
         nova_string += 'R'
    else:
        nova_string += letra

    contador += 1

print(nova_string)