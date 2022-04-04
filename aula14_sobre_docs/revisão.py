'''

REVISÃO AULA 14 - 14/03/22

'''

# EX

num1 = input('digite um numero: ')
num2 = input('digite outro numero: ')
# isnumeric - isdigit - isdecimal
# somente ira checar numeros positivos;
# print(num1.isnumeric()) #retornara valor booleano
# print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Nao foi possivel executar')
