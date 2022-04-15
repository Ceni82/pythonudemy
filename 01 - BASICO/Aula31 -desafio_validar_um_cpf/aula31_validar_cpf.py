'''

AULA 31 - DESAFIO VALIDAR UM CPF

 -------------------------------
 INSTRUÇÕES (EX)

CPF - 168.995.350 - 09
1 * 10 = 10            #    1 * 11 = 11 <-
6 * 9 = 54             #    6 * 10 = 60
8 * 8 = 64             #    8 * 9 = 72
9 * 7 = 63             #    9 * 8 = 72
9 * 6 = 54             #    9 * 7 = 63
5 * 5 = 25             #    5 * 6 = 30
3 * 4 = 12             #    3 * 5 = 15
5 * 3 = 15             #    5 * 4 = 20
0 * 2 = 0              #    0 * 3 = 0
        297            # -> 0 * 2 = 0
                       #          343
11 - (297 % 11) = 11   #   11 - (343 % 11) = 9
11 > 9 = 0             #    Digito 2 = 9
Digito 1 = 0           #
______________________________________
 *peguei esse no google!
 CPF - 203.149.108-05 (mauz ai Gustavo)
'''
#
# #203149108
#


cpf = [0,0,4,7,6,5,0,9,0]
num = [10,9,8,7,6,5,4,3,2]
num2 = [11,10,9,8,7,6,5,4,3,2]
var1 = []
var2 = []
soma = 0
soma2 = 0
for a, b in enumerate(cpf):
    var1.append(b * num[a])
    print(var1)
for valor in var1:
    soma = soma + valor
    print(soma)
calc1 = soma % 11
print(calc1)
if calc1 > 9:
    print(1)
else:
    print(0)
    calc1 = 0
# print(calc1)
calc2 = calc1
cpf.append(calc2)
for a, b in enumerate(cpf):
    var2.append(b * num2[a])
    print(var2)
for valor in var2:
    soma2 = soma2 + valor
    print(soma2)
calc3 = soma2 % 11
print(calc3)

#sim ta bem porcaria, mas eu  feliz demais pq eu consegui começar a caminhar sozinho!