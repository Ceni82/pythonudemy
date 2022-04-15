'''
EXERCICIO 3

'''

nome = input('Digite seu nome: ')
qnt_carac = len(nome)

if qnt_carac <= 4:
    print("Teu nome é muito pequeno!")
elif qnt_carac == 5 or qnt_carac == 6:
    print('Teu nome é normal!')
elif qnt_carac >= 8:
    print (' Teu nome é muito grande!')
else:
    print()