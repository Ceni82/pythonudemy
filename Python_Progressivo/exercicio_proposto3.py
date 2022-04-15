'''
EXERCICIO PROPOSTO 3 - 06/03/22

IF / ELSE

Crie um programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

print('Digite a letra conforme exemplo abaixo!')
print('\'M\' se masculino;')
print('\'F\'se feminino;')
valor = input('Digite o valor escolhido: ')


if valor == 'm':
    print('Masculino')

else:
    if valor == 'f':
        print('Feminino')
    else:
        print('Valor invalido')


