'''
AULA 16 FORMATANDO VALORES - 22/03/22 (UDEMY)

:s - Texto (strings)
:d - Inteiros (int)
:f - Numeros de ponto flutuantes (float)
:. (NUMERO)+f - Quantidade de casas Decimais (float) - ex:.1f, .4f;
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s,d ou f)

 onde os numeros serao adicionados)
 > - Esquerda
 < - Direita
 ^ - Centro

'''

num_1 = 1
print(f'{num_1:0>10}') #vai add os "000" no inicio do numero (esquerda)
num_2 = 1150
print(f'{num_2:0<10}')# vai add os "00" no final do numero (direita)
num_3 = 234
print(f'{num_3:0^10}')# vai add os "00", no inicio e no fim deixando o numero no meio
num_4 = 243 # tbm transformar o numero em float
print(f'{num_4:.2f}')
# ou add "00" (numeros)
print(f'{num_4:0>10.2f}')
#funciona dom strinds too
#EX
nome = 'mateus ceni'
# print(len(nome))
print(len('###################'))
# print (( 50 - len(nome) / 2)) # contar quantos caracteres tem no meu nome
# print (f'{nome:#^50}')

#formatando nome outro EX
nome = 'mateus ceni'
nome_formatado = '{:$^18}'.format(nome)
print(nome_formatado)
