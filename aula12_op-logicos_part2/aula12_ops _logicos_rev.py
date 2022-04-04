'''
Operadores Logicos
 and, or, not, in & not in


a = 2
b = 2
c = 3

print (a == b and b < c) # 'a' é igual a 'b' e 'c é maior q 'b' portanto é True
print(a == b or b < c) # nesse caso mudo o 'and' por 'or' mas ainda assim o valor sera True
print(not a == b and b < c) # o 'not' inverte as expressõe tornando 'False'
'''

# o AND (and) vai comparar de os 'valores' comparados foram verdadeiros ou
# falso tendo um valor falso ele retorna falso

# quando utilidado o OR 'or' ele retornara True se qualquer um dos valores for verdadeiro

# mostrando como o NOT (not) funciona
# a = 2
# b = 3
# if b > a: #sem o not
#     print( 'B maior q A.')
# else:
#     print(' A maior q B.')
#
# if not b > a:  # usando o not
#     print('B maior q A.')
# else:
#     print('A maior q B.')

# EXEMPLO IN (in)

# nome = "mateus ceni"
#
# if 'bn' in nome:
#      print (' Seeeem')
# else:
#      print('nom')

nome = input('Login: ')
senha = input('Senha: ')

nomeBd = 'Mateus'
senhaBd = '12345'

if nomeBd == nome and senhaBd == senha:
    print('Logado')
else:
    print('Usuario ou senha invalidos')