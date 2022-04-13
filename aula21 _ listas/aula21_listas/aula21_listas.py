'''

AULA 21 - LISTAS - 21/02/22

fatiamento
appenr, insert, pop, del, clear, extend, +
min, max
range

# indices 0    1    2    3    4
lista = ['a', 'b', 'c', 'd', 'e']
#negativo 5    4    3    2    1
lista [3] = 'qq outra coisa'
string = "abcde"
print(lista)

#-------------------------

# indices 0    1    2    3    4
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[0:4])


#-----------
# indices 0    1    2    3    4    5
lista = ['a', 'b', 'c', 'd', 'e', 10.5]
print(lista[2:])
#---------------------
# indices 0    1    2    3    4    5
lista = ['a', 'b', 'c', 'd', 'e', 10.5]
print(lista[: : -1])


l1 = [1,2,3]
l2 = [4,5,6]
l1.extend('a')
print(l1)
print(l2)

#-------------------
# inserir
l1 = [1,2,3]
l2 = [4,5,6]

l2.insert(0, "banana")

print(l1)
print(l2)
print(l2)
#-----------------

l2 = [4,5,6]
print(l2)
l2.insert(0, "banana")
print(l2)
l2.pop()
print(l2)
#-----------------

#delet
#ind  0 1 2 3 4 5 6 7 8
l2 = [1,2,3,4,5,6,7,8,9]
l2.insert(0, 'banana')
print (l2)
del (l2[0])
print(l2)

#----------------
# max min
#ind  0 1 2 3 4 5 6 7 8
l2 = [1,2,3,4,5,6,7,8,9]
print(max (l2))
print(min(l2))

#--------------------

l2 = list(range(1,100,8))
print(l2)

#__________________
l2 = list(range(1,100,8))
for valor in l2:
    print(valor)
'''
#-----------------
#ind  0 1 2 3 4 5 6 7 8
# l2 = [1,2,3,4,5,6,7,8,9]
#
# soma = 0
# for valor in l2:
#     soma = soma + valor
# print(soma)
'''
#---------------

l2 = ['String', True, 10, -10.5]
for elen in l2:
    print(f' O tipo de elen é {type(elen)} e sei valor é {elen}')

'''

#----------------------

secreto = 'perfume'
digitadas = []
chances = 5
while True:
    if chances <= 0:
        print(' Vc perdeu!!')
        break

    letra = input(' Digite uma letra: ')
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f' HHUUUL, a letra "{letra}" existe na palavra secreta!')
    else:
        print(f'AFFFFSSSS, a letra "{letra}" NÃO existe na palavra secreta!')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
       print(f'VC ganhou!aA palavra era {secreto_temp}')
       break
    else:
       print(f'A palavra secreta está assim: {secreto_temp}')

    if letra not in secreto:
        chances -= 1
    print(f' Vc ainda tem {chances} chances.')
    print()