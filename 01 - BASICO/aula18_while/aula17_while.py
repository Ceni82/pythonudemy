'''
AULA 17 - WHILE
Utilizado para realizar ações enquanto uma condição é verdadeira

Requisitos: Entender condiçoes e operadores!  (while: enquanto)
'''
# while condicao:
    # pass
#-------------------------------
# while True: #loop infinito
#     nome = input('Qual o seu nome?')
#     print(f' Olá {nome}!')
# print(f'Não sera executada')

#--------------------------------
# x = 0
# while x < 5:
#     print(x)
#     x = x +1
#
# print('Fim!')

 #----------------------------
# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         break #ou continue
#     print(x)
#     x = x + 1
#
# print('Fim!')
#
# -----------------------------------
#
# x = 0 #coluna
#
# while x < 10:
#     y = 0  # linha
#     while y < 5:
#         print(f'{x},{y}')
#         y += 1
#
#     x += 1 # é igual a fazer x = x + 1
#
# print('Fim!')
#  -----------------------------------

while True:
    print()
    num1 = input('Digite um numero:')
    num2 = input('Digite outro numero:')
    op = input('Digite o operador:')
    sair = input ('Deseja Sair? [s]im ou [N]ão: ' )

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Vc precisa digitar um numero valido ou sair:')
        continue
    num1 = int(num1)
    num2 = int(num2)
# + - / *

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '*':
        print(num1 * num2)
    else:
        print("Operador Invalido!")