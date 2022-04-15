'''

revisando listas - 05/04/22

fastiamento
append, insert, pop, clear, extend, + min , max
range

ex
booleanos = True or False
inteiros = 10
flutuantes = 1.23
str = 'txt'
'''
# lista = [ 'a', 'banana', 'c', 'd', 10, 3 ]
# lista[3] = ' teste'
# # string = 'abcde'
#
# print(lista[3])

# lista = [ 'a', 'b', 'c', 'd', 10, 3 ]
# print(lista[::-1])

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista3 = lista1 + lista2
# print(lista1)
# print(lista2)
# print(lista3)

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista1.extend('a')
# print(lista1)
# print(lista2)

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
#
# lista2.append('d')
# print( lista2[3])
#
# print(lista1)
# print(lista2)

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
#
# lista2.insert(6, 'batata')
# print(lista1)
# # print(lista2)

#
# lista2 = [4, 5, 6]
# print(lista2)
# lista2.insert(0, 'banana')
# print(lista2)
# lista2.pop()
# print(lista2)


#
# lista2 = [1,2,3,4,5,6,7,8,9]
# print(lista2)
# del (lista2[3:5])
# print(lista2)


#
# lista2 = [1,2,3,4,5,6,7,8,9]
# print(max(lista2))
# print(min(lista2))

#
# lista2 = [1,2,3,4,5,6,7,8,9]
#
# soma = 0
# for valor in lista2:
#     soma = soma + valor
#
# print(soma)
#
# lista2 = ['str', True, 10, -20.56]
#
# for elem in lista2:
#     print(f' {type(elem)} igual a {elem}')


secret = 'perfume'
digit = []
chances = 4
while True:
    letra = input('Digite uma letra:')

    if len(letra) > 1:
        print(' digite so uma letra')
        continue
    digit.append(letra)
    if letra in secret:
        print(f'deu boa! a letra {letra} existe ')
    else:
        print(f' a letra {letra} não existe na palavra!')
        digit.pop()

    secreto_temp = ''
    for letra_secreta in secret:
        if letra_secreta in digit:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    if secreto_temp == secret:
        print(f'deu boa!!! a palavra era {secreto_temp}')
        break
    else:
        print(f' a palavra secreta esta assim: {secreto_temp}')

    if letra not in secret:
        chances -= 1
    print(f' vc ainda tem {chances} chances')
    print()