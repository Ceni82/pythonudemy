'''

ALGORITMO TREINO - FAZENDO CAFÉ
'''

print('BOM DIA !! BORA FAZER UM CAFEZINHO?!')
nome = input('Qual seu nome? ')
pergunta1 = input(f'{nome} vc gosta de cafe?')
sim = ('sim')
nao = ('não')
if pergunta1 == sim:
    # sim = True
    print('Quem bom!!  Eu tbm!')
    fazer = input(f'{nome}!! Bora fazer um?? ')
    if fazer == sim:
        print('Peque o pó do café!!')
        ter = input(f'{nome} tem café ai né?' )
        if ter == sim:
            print('Ufa!! achei que não tinha!!')
            print('Abra a cafeteira e adicione 3 dosadores cheios!')
            quant = input('Tem café suficiente para tres dosadores? ')
            if quant == sim:
                print('Otimo!!')
            else:
                print(f"{nome} talvez fique aguadinho!")
            print(f'{nome} agora q vc ja colocou as doses do pó, temos que adcionar agua nessa cafeteira!')
            cafet = input('É cafeteira né? ou coador?')
            cafeteira = ('cafeteira')
            coador = ('coador')
            if cafeteira:
                print('Top!! Tbm tenho uma! A minha é do "Star Wars!')
                print('Coloque agua até o marcador!')
                print('Feche a tampa ligue!!')
                botao = input('Naquela botão vermelho ali!! achou? ')
                if botao == sim:
                    print('Ligue-o, e agora é so aguardar!')
            elif coador:
                print('Certo! Minha namorada usa tbm!!')

    else:
        print(f'Tu vai ter de ir comprar café {nome}!!')
elif pergunta1 == nao:
    print('Que pena!! Não sabe o q ta perdendo!')
else:
    print()
