'''
 EXERCICIO PROPOSTO 03 - IF ELIF ELSE - 12/03/22

 3. Faça um Programa que leia três números inteiros e mostre o maior deles.
 >soluçao site
    primeiro = int(input('Primeiro numero: '))
    segundo  = int(input('Segundo numero : '))
    terceiro = int(input('Terceiro numero: '))

    maior = primeiro

    if (segundo > maior):
        maior = segundo
    if (terceiro > maior):
        maior = terceiro

    print('Maior: ',maior)


Não se assuste se não entender de cara.
Leia, releia, pense, pense de novo, reflita, chore em posição fetal até entender.

'''
 #meu code :(
num1 = int(input('Digite o primeiro numero: ' ))
num2 = int(input('Digite o segundo numero: ' ))
num3 = int(input('Digite o terceiro numero: ' ))

if num1 > num2 and num1 > num3:
    print(f'O numero {num1} é o maior!')
elif num2 > num1 and num2 > num3:
    print(f'O numero {num2} é o maior!')
else:
    print(f'O numero {num3} é o maior!')