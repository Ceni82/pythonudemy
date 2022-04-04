# '''
# OPERADORES RELACIONAIS
# == > >= < <= !=
# '''
#
# # = é igual a igual AFIRMANDO que é igual
# # == dois sinais de igual (==) eu to PERGUNTANDO de os valores sao iguais
#
# print( 2 == 3 ) #False
# print( 2 == 2 ) #True
#
# # outro EX
#
# num1 = 2 #int
# num2 = '2' #str
# print(num1 == num2) # é flso pq uma variavel é int e a outro é uma str
#
# # outro ex (essa vai dar TRUE)
#
# num1 = 2 #int
# num2 = 2 # int
#
# expressao = ( num1 == num2 )
#
# print(expressao)
#
# # outro EX com outro operador
#
# num1 = 3 #int
# num2 = 2 #int
#
# expressao = ( num1 >= num2 )
# # >= <= a junção de > ou < com =
# print(expressao)
#
#
# # outro com !=
#
#  # != sinal diferente
#
# num1 = 2 #int
# num2 = 2 #int
#
# expressao = ( num1 != num2 )
#
# print(expressao)
#
# #exercicio
# print()
# print('------------------------------')
# print()
#
# nome = input("qual teu nome: ")
# idade = input('qual tua idade:')
#
# idade = int(idade)
# maior_de = 18
#
# if idade >= maior_de:
#     print(f' {nome} pode pegar emprestimo')
# else:
#     print (f' {nome} não pode pegar emprestimo')
#

nome = input("qual teu nome: ")
idade = input('qual tua idade:')

idade = int(idade)
# limites de idade
menorDe = 20
maiorDe = 30

if idade >= menorDe and idade <= maiorDe:
    print(f' {nome} pode pegar emprestimo')
else:
    print (f' {nome} não pode pegar emprestimo')
