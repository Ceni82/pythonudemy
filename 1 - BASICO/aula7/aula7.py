nome = 'Mateus Ceni'
idade = 39 #int
altura = 1.77 #float
e_maior = idade > 18 #booleano
peso = 95 #int
imc = peso/(altura*altura)
#print('Nome:', nome)
#print('Idade:', idade)
#print('Altura:',altura)
#print('É maior de idade:', e_maior)

#print('O ', nome , 'tem ', idade,'anos de idade, e seu imc', imc, 'é!')
# AULA 7 aqui
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
#ou
print('{} tem {} anos e seu imc é {}.'. format(nome, idade, imc))
#ou
print('{0} tem {1} anos e seu imc é {2}.'. format(nome, idade, imc))
#ou
print('{n} tem {i}anos e seu imc é {im:.2f}.'. format(n=nome, i=idade, im=imc))
