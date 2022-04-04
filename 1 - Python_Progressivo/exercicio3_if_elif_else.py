'''

EXERCICIO 3 - 02/03/22 - If, elif & else:

3. Faça um Programa que leia três números inteiros e mostre o maior deles.
'''

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num1 > num2 or num1 > num3:
    print(num1)
elif num2 > num1 or num2 > num3:
    print(num2)
elif num3 > num2 or num3 > num1:
    print(num3)


