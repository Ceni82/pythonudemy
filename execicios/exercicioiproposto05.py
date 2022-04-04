'''

EXERCICIO PROPOSTO - 13/03/22
6. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

valor1 = int(input('Digite primeiro valor: '))
valor2 = int(input('Digite segundo valor: '))
valor3 = int(input('Digite terceiro valor: '))



maior = valor1
menor = valor1


if (valor2 > maior):
    maior = valor2

elif (valor2 < maior):
    menor = valor2
if (valor3 > maior):
    maior = valor3
elif (valor3 < maior):
    menor = valor3

meio = valor1
if (valor3 > maior or valor2 > maior):
    meio = valor1
elif (valor3 < maior or valor2 < maior):
    meio = valor1

print('Maior: ', maior)
print('Meio : ', meio)
print('Menor: ', menor)
