'''

EXERCICIO 01 - IF, ELIF & ELSE - PYTHON PROGRESSIVO - 11/03/22

  Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

  char=input('Digite um caractere: ')

    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or \
       char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
           print('Vogal')
    else:
           print('Consoante')
'''

#minha resolução

letra = str(input('Digite uma letra: '))

if letra =="a" or letra =='e' or letra =='i' or letra =='o' or letra =='u':
    print(f'{letra.upper()} é uma vogal!')
elif letra == '1' or letra == '2' or letra == '3' or letra == '4' or letra == '5' \
        or letra == '6' or letra == '7'or letra == '8' or letra == '9' or letra == '0':
    print(f'{letra} é um valor invalido!')
else:
    print(f'{letra.upper()} é uma consoante!')