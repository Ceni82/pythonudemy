'''

 EXERCICIO 2 - 02/03/22 - If, elif, Else

2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média
do aluno e dar o seguinte resultado:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
#
# nota1 = input('Digite a primeira nota: ')
# nota2 = input('Digite a segunda nota: ')
# media = int(nota1) + int(nota2)
#
# if media == 10:
#     print('Aprovado com Distinção')
# elif media > 10:
#     print("Favor confira suas nota e digite um valor valido!")
# elif media >= 7:
#     print('Aprovado')
# elif media < 7:
#     print('Reprovado')
# else:
#     print()

# SOLUÇÃO DO SITE
# ttl = 'solução do site'
# up = ttl.upper()
# print(up)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print('Media: ',media)

if media<7.0:
    print('Reprovado')
elif media<10:
    print('Aprovado')
else:
    print('Aprovado com Distinção!')