'''


Rsivão while

while = enquanto
'''

# while True: #loop infinito
#     nome = input('Qual teu nome:')
#     print(f'Olá {nome}!')
# print('Não sera executado')

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         break
#     print(x)
#     x = x + 1
# print(f' Finishhh')
#
# x = 0
#
#
# while x < 10:
#     y = 0
#
#     while y < 5:
#         print(f' X vale {x} e Y vale {y}')
#         y += 1
#     x += 1 # equivale a x = x +1
#
# print(f'Acabou!')

while True:
    print()
    num_1 = input('digite uma numero:')
    num_2 = input('digite outro numero:')
    operador = input('digite um operador:')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('digite um valor valido!')
        continue


    num_1 = int(num_1)
    num_2 = int(num_2)


    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Op invalido')