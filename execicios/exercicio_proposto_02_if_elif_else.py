'''

EXERCICIO PROPOSTO - IF, ELIF, ELSE - 12/03/22

2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a
média do aluno e dar o seguinte resultado:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

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

'''

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = nota1 + nota2

if media < 7:
    print('Reprovado!')
else:
    if media > 10: # Errei aqui
        print('Aprovado com distinçao!')
    else:
        print('Aprovado!')
