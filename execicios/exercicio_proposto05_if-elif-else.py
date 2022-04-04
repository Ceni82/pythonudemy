'''
EXERCICIO POROPOSTO 05 - 13/03/22

 5. Faça um programa que pede dois inteiro e armazene em duas variáveis.
 Em seguida, troque o valor das variáveis e exiba na tela.

 O segredo é: usar uma variável auxiliar, a aux

A função dar aux é guardar aquele primeiro valor contido em var2.
Então, a troca de valores se dá assim:

aux = var2
var2 = var1
var1 = aux

Faz sentido pra você?
Reflita e veja se entender perfeitamente, pois esse algoritmo de troca é MUITO importante!


    var1 = int(input('Primeiro numero: '))
    var2  = int(input('Segundo numero : '))

    print('Variavel 1: ',var1)
    print('Variavel 2: ',var2)
    print('Invertendo...')

    aux  = var2
    var2 = var1
    var1 = aux

    print('Variavel 1: ',var1)
    print('Variavel 2: ',var2)
'''


valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))


print('Variavel 1: ', valor1)
print('Variavel 2: ', valor2)
print('Invertendo...')

aux = valor2
valor2 = valor1
valor1 = aux

print('Variavel 1: ', valor1)
print('Variavel 2: ', valor2)