'''

AULA 01 - INTERMEDIARIO - DEF (PARTE_1) - 15/04/22

DEFINIR PROPRIAS FUNCOES (DEF)
'''

# def funcoes():
#     print('balder, gato fidido!')
#
# funcoes()
# funcoes()
# funcoes()
# # pra entender o pq usar funções,
# # eu preciso alterar uma unica X,
# # no print somente, seria em todas:
# print('balder, é gato fidido!')
# print('balder, é gato fidido!')
# print('balder, é gato fidido!')

#-----------------------------

# def mandandooi(msg ='e ai!!', nome = 'BALDER'):
#     nome = nome.replace('d', '6')
#     msg = msg.replace('o', '1')
#     print(msg, nome)
#
# mandandooi(' oiiiiii!', 'balder')
# mandandooi(' e ai!', 'balder')
# mandandooi()
# mandandooi(' oiiiiii!', 'gato fidido')
# mandandooi(nome = 'baldinho', msg = 'olá')


#---------------------------

def mandandooi(msg ='e ai!!', nome = 'BALDER'):
    nome = nome.replace('d', '6')
    msg = msg.replace('o', '1')
    return f'{msg} {nome}'

var = mandandooi()

print(var)
