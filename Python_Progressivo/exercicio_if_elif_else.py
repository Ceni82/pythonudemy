'''

EXERCICIO IF, ELIF e ELSE

 (https://www.pythonprogressivo.net/2018/02/Exercicios-Python-IF-ELIF-ELSE.html)

 28/02/2022
 Exercicio proposto:
 1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

# vogais = ['a','e','i','o','u' ]
# consoante = ['b','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
let_dig: str = input('Digite uma letra: ')

if let_dig == '1' or let_dig == '2' or let_dig == '3' or let_dig == '4' or let_dig == '5' or let_dig == '6' or let_dig == '7' or \
     let_dig == '8' or let_dig == '9' or let_dig == '0':
    print('Digite somente letras!')
elif (let_dig == 'a') or (let_dig == 'e') or (let_dig == 'i') or (let_dig == 'o') or (let_dig == 'u'):
    print(f'Você digitou a letra {let_dig}, e essa letra é uma Vogal!')
elif let_dig != ():
    print(f'Você digitou a letra {let_dig}, e essa letra é uma Consoante!')
else:
   print()

#  RESOLUÇAO DO SITE (o meu ficou bem mais bonito)
#    char=input('Digite um caractere: ')
#
#     if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or \
#        char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
#            print('Vogal')
#     else:
#            print('Consoante')
# # ponto a observar aqui (AS LETRAS MAIUSCULA)
#
# # SOBRE OS NUMERO (vai e o usuario digite ne)
# char= input('Digite a letra: ')
# if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or\
# char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
# print('Vogal')
# else:
# if char=='1' or char=='2' or char=='3' or char=='4' or char=='5' or\
# char=='6' or char=='7' or char=='8' or char=='9' or char=='0':
# print('Invalido')
# else:
# print('Consoante')
