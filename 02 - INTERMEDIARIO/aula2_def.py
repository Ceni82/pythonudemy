'''
AULA 02 - INTERMEDIARIO - DEF (parte2) - RETURN - 15/04/22
'''

# def funcao(var):
#     return var
#     print(' isso nao aparece')
#
# variavel = funcao (' meu valor 1')
#
# if variavel:
#     print(variavel)
# else:
#     print('sem valor')

#--------------------------------

# def divisao (n1, n2):
#     if n2 > 0:
#         return n1 / n2
#
# divide = divisao(3,0)
#
# if divide:
#     print(divide)
# else:
#     print('conta invalida')

#----------------------------------
#
# def divisao (n1, n2):
#     if n2 == 0:
#         return
#     return n1 / n2
#
#
# divide = divisao(8,4)
#
# if divide:
#     print(divide)
# else:
#     print('conta invalida')

#-------------------------------------------

# def dumb():
#     return True
# var = dumb()
# print(var,  type(var))

# #------------------------------
#
# def f(var):
#     print(var)
# def dumb():
#     return f
# # print(type(f))
# var = dumb()
# # print(id(var), id (f))
# #
# #
# # if var == f:
# #     print('var e igual a f')
# # else:
# #     print('nao vai')
#
# var('pode executar')

#----------------------------------------

def dumb():
    return 'mateus', 'ceni'

# print(dumb())

var = dumb()
print(var[0], type(var))