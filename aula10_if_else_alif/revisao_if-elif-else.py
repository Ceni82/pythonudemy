'''
Revisão IF, ELIF, ELSE

if True:
    print("verdadeiro")

    num1 = 2
    num2 = 4
    print(num1 + num2)
if False:
     print ('Verdadeiro')
print('é falsa')

if False:
     print('Verdadeiro')
else:
    print('falso')

'''

if False: #se
     print ('Verdadeiro')
elif True: #se não - é usado quando pŕecisamos verificar outra condição;
    print('esse sim é true')
    print('isso é um teste')
    print('para testar a hierarquia')
    print('nas outras não vou por nada pq nem vai aparecer'
           'mas podia'
elif True:
    print(' e agora')
else:
    print('nao deu')