'''
AULA 19 - ITERANDO STRINGS COM WHILE- 19/02/22

'''
# Indice
#       0123456789.......................33
frase = "O rato roeu a roura do rei de roma"
tamanho_frase = len(frase)
contador = 0
nova_string = ''

imp_do_user = input("qual letra vc quer colocar em maiusculo:")
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == imp_do_user:
        nova_string += imp_do_user.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)