'''

REVISAO LEN - 09/03/22 retomada dia 14/03/22

 - LEN serve para contar o numero de caracteres de uma STR(string) e outros tipos dados
mas, nao funciona com tipos numericos ( INT e FlOAT);
- Ele conta espaços;
- so pra lembrar, input sempre entraga uma STR
'''


user = input('Digire seu user: ')
qnt_carac = len(user)

print(user, qnt_carac, type(qnt_carac))

if qnt_carac < 6:
    print('Vc precisa digitar pelo menos 6 caracteres')
else:
    print('Vc foi cadastrado no sistema!')


# str1 = input('digite algum a coisa: ')
# str2 = input('digite outras coisa: ')
#
# print(f'a quantidade de caracteres digitadas foi {len(str1 + str2)}')
#
# # dois EX de como fazer a função LEN:
# print(len(str2))
# print(str2.__len__())