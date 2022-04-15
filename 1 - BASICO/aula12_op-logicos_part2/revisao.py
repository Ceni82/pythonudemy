nome = input("qual teu nome: ")
idade = input('qual tua idade:')

idade = int(idade)
# limites de idade
menorDe = 20
maiorDe = 30

if idade >= menorDe and idade <= maiorDe:
    print(f' {nome} pode pegar emprestimo')
else:
    print (f' {nome} não pode pegar emprestimo')
