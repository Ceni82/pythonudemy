'''
operadores logico parte 2

and, or, not, in e not in


comparação1 and comparação #as duas presisam ser verdadeiras para retornar verdadeiro


comparação or comapração # apenas uma precisa ser verdadeira



#not
a = 2
b = 3

if not b > a:
        print ("B é maor e A.")
else:
        print (' B não é maior q A')


nome = "mateus"
if 'te' not in nome:
        print ('nao')
else:
        print('sim')
'''

user = input(' Nome do usuario: ')
senha = input(' Senha do usuario: '
              '')

usuario_bd = 'mateus'
senha_bd = '1234'

if usuario_bd == user and senha_bd == senha:
        print (' Acesso autorizado')
else:
        print (' Usuario ou senha invalidos')