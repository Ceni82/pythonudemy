'''
 FAÇA UM PROGRAMA Q PEÇA AO USER PARA DIGITAR UM INT,
 INFORME SE ESTE MUMERO É PAR OU IMPAR. CASO O USER NÃO
 DIGITAR UM INT, INFORME Q NAO É UM INT.
% = esse representa resto
'''



print('DIGITE UM NUMERO INTEIRO!')

valor = input('Digite um valor: ')


if valor.isnumeric():
    valor = int(valor)
    if (valor%2) == 0:
        print(f'O {valor} é um numero Par!')
    else:
        print(f' O {valor} é um numero Impar')
else:
    print(f'O {valor} é um caracter invalido')




