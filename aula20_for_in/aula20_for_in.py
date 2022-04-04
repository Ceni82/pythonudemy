'''

AULA 20 - FOR IN - 21/02/22

For in em Python
Iterando stringd com for
Função range(star=0, stop, step=1)
'''

texto = 'Python'

for letra in texto:
    print(letra)
#--------------------------

for numero in range(10): #(5,10) conta de 5 a 10, (5,20,2) conta de 5 até 20 pulando de 2 em 2;
    #(20, 10, -1) para contagem decrecente;
    print(numero)

#-----------------------

for numero in range(0, 100, 8):
    print (numero)
#--- mesma coisa
print ('_________________')
for numero in range(100):
    if numero % 8 == 0:
        print(numero)

#__________________

texto = 'Python'
nova_str = ''

# continue - pula pro proximo laço
# break - termina a iteração

for letra in texto:
    if letra == 't':
        nova_str += letra.upper()
    elif letra == 'h':
        nova_str += letra.upper()
    else:
        nova_str += letra
print (nova_str)