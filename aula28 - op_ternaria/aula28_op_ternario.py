'''

oprador ternario - 08/04/22
'''

# logged_user = True
#
# if logged_user: # igual if logged_user == True:
#     msg = 'user logado'
# else:
#     msg = "precisa logar"
#
# print(msg)


# com OP. TENARIO

# logged_user = True
# msg = 'user logado' if logged_user else "precisa logar"
# print(msg)

#outro EX

# idade = 18
# if idade >= 18:
#     print('pode acessar')
# else:
#     print('não pode acessar')
#
# OU

idade = input('qual tua idade?')
if not idade.isnumeric():
    print('Vc precisa digitar apenas numeros!')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'não pode acessar'

print(msg)