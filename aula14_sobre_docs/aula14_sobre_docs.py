'''
DOCUMENTAÇÃO
'''

num1 = input('digite um numero: ')
num2 = input('digite segundo numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print (num1 + num2)
else:
    print ('valor invalido')

