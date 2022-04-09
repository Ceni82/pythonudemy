'''
AULA 30 - EXERCICIO DE REPETIÇÃO  - FOR / WHILE - 08/04/22
'''

#USEI o WHILE

contador = 0
contador2 = - 10
while (contador < 9):
    print(contador, abs(contador2))
    contador = contador + 1
    contador2 = contador2 + 1

print('___________________________')
#Resolução UDEMY - com o FOR... ':|' - bom a ideia era ter esse resultado!

for p, r in enumerate(range(10, 1,-1)):
    print(p, r)
