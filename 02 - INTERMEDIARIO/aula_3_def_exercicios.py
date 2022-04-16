'''

EXERCICIOS DEF

'''
'''
1 - CRIAR UMA FUNÇÃO QUE EXIBE UMA SAUDAÇÃO COM OS PARAMETROS SAUDAÇÃO E NOME;
'''
# def funcao(oi, nome):
#     print('Olá', 'Balder')
#
# funcao('oi', 'nome')
#---------------------------------
'''
2 - CRIE UMA FUNÇÃO Q RECEBA 3 NUMEROS COMO PARAMETROS E 
EXIBA UMA A SOMA ENTRE ELES;
'''
# def somar():
#     n1 = float(input('digite o primeiro numero:'))
#     n2 = float(input('digite o segundo numero:'))
#     n3 = float(input('digite o terceiro numero:'))
#     somar = n1 + n2 + n3
#     print("Soma:", somar)
# somar()

#---------------------------------------

'''
3 - CRIE UMA FUNÇÃO Q RECEBA 2 NUMEROS. O PRIMEIRO É UM VALOR E O SEGUNDO 
UM PERCENTUAL (EX.10%). RETORNE (RETURN) O VALOR DO PRIMEIRO NUMERO SOMADO DO
AUMENTO DO PERCENTUAL DO MESMO.
'''

# def calc():
#     n1 = float(input('digite o primeiro numero:'))
#     n2 = float(input('digite o segundo numero:'))
#     calc = (n2 * n1 / 100) + n1
#     print("Calculo de porcentagem:", calc)
#     return
# calc()

'''
4 - Fizz Buzz -  SE O PARAMENTRO DA FUNÇÃO FOR DIVISIVEL POR 3, RETORNE fIZZ,
SE O PARAMETRO DA FUNÇÃO FOR DIVISIVEL POR 5, RETORNE BUZZ. sE O PARAMETRO DA FUNÇÃO FOR
DIVISIVEL POR 5 E POR 3, RETORNE FizzBuss, CASO CONTRARIO, RETONE O NUMERO ENVIADO;
'''

def exFizzBuss(n1):#não terminei

    if n1 % 5 == 0 and n1 % 3 == 0:
      return 'FizzBuss'
    elif n1 % 5 == 0:
      return 'BUZZ'
    elif n1 % 3 == 0:
      return 'FIZZ'
    else:
      return (n1)

n1 = float(input('digite um numero:'))
exFizzBuss(n1)