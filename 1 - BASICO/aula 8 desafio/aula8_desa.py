'''
* Criar variaveis para nome (str), idade (int), altura (float), e peso (float) de uma pessoa;
* Criar criar variavel para ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto co mtodos os valores na tela usando F-strings (com as chaves)
'''

nome = 'Mateus' #str
idade = 39 #int
altura = 1.77 #float
peso = 95.300 #flout
imc = peso / altura ** 2
anoAtual = 2022 #int
anoNascimento = anoAtual - idade

print(f'O {nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC do {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {anoNascimento}')