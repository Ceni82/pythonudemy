'''
EXERCICIO 1 AULA - IF ELSE

Faça um programa que peça dois números e imprima o maior deles.
'''

# num1 = int(input('Digite um numero: '))
# num2 = int(input('Digite outro numero:'))
# 
# if num1 > num2:
#     print(f'O numero {num1} e maior q o {num2}!(Oi eu sou o IF)')
# else:
#     print(f'O numero {num2} e maior q o {num1}!(Oi eu sou o ELSE)')

num1=int( input('Digite o primeiro numero: ') )
num2=int( input('Digite o segundo numero: ') )

if num1 > num2 :
    print('O primeiro, %d, é maior' %num1)
else:
    if num1 == num2 :
        print('Os números são iguais')
    else:
        print('O segundo, %d, é maior' %num2)
        
        