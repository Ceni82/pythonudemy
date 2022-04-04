'''
Operadores relacionais
== . igualdade
> . Maior Q
>= . Maior q ou igual a
< . Menor Q
<=. Menosq ou igual a
!=. Diferente



 print( 2 == 1 )
#____________________________

num1 = 2 #int
num2 = '2' #string
#print (num1 == num2)

---------------------------

num1 = 2
num2 = 2
expressao = (num1 == num2)
print (expressao)

#--------------------

num1 = 3 #int
num2 = 2 #int
expressao = (num1 >= num2)
print (expressao)



nome = input (' Qual seu nome: ')
idade = input ('Qual sua idade: ')
idade = int(idade)

#limite para pegar imprestimo

idade_limite = 18

if idade >= idade_limite:
     print (f'{nome} pode pegar o imprestimo')
else:
     print (f'{nome}- NÃO PODE PEGAR IMPRESTIMO')

'''
nome = input (' Qual seu nome: ')
idade = input ('Qual sua idade: ')
idade = int(idade)

#limite para pegar imprestimo
menor_idade = 20 #menor idade
maior_idade = 30 #idade limite
if idade >= menor_idade and idade <= maior_idade:
     print (f'{nome} pode pegar o imprestimo')
else:
     print (f'{nome}- NÃO PODE PEGAR IMPRESTIMO')