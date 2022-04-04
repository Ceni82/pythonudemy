'''
EXERCICIO 01
'''
# MEU COD. NAO FUNCIONOU TOTAL =(!

# num = input('Digite um numero: ')
# num = int(num)
# resto = num % 2
#
# if resto == 0:
#     print(f'O numero q vc digitou é o {num} e ele é um numero par!')
# elif resto != 0:
#     print(f'O numero q vc digitou é o {num} e ele é um numero impar!')
# else:
#     print(f' Favor digitar somente numeros inteiros!')

# RESOLUÇÃO

# num_int = input(' Digite um numero inteiro: ')
#
# if num_int.isdigit():
#     num_int = int(num_int)
#
#     if num_int % 2 == 0:
#         print(f' {num_int} é par!')
#     else:
#         print (f'{num_int} é impar!')
# else:
#     print ('Isso não é um numero inteiro!')

# ex 2

num_int = input(' Digite um numero inteiro: ')

if not num_int.isdigit():
    print('Isso não é um numero inteiro!')

else:
    num_int = int(num_int)

    if not num_int % 2 == 0:
        print(f' {num_int} é par!')
    else:
        print(f'{num_int} é impar!')

