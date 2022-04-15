'''
AULA 29 - Expressao condicional com OR

'''

#
# nome = input('Qual seu nome?')
#
# if nome:
#     print(nome)
# else:
#     print('vc nao digitou nada!')

# USANDO OR

# nome = input('Qual seu nome?')
# print(nome or 'vc nao digitou nada!')
# EX print(nome or None or False or 0 or 'vc nao digitou nada!')

a = 0 #false
b = None #false
c = False #false
d = [] #false
e = {} #false
f = 22 #true
g = 'mateus' #true

variavel = a or b or c or d or e or f or g

print(variavel)

