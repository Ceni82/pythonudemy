'''
FAÇA UMA PROGRAMA Q PERGUNTE A HORA AO USER, BASEADO NISSO USE A SAUDAÇÃO ESPECIFICA PARA AQUELE
MOMENTO DO DIA - (BOM DIA 0-11, BOA TARDE 12-18 OU BOA NOITE 19-23
18-03-22
'''

# nome = input('Qual seu nome:')
hora = input(f' vc sabe que horas são: '.2f)

if hora.isdigit():
    hora = float(hora)
    if hora < 11:
       print('Bom dia')
    elif hora == 12 or hora < 18:
       print('Boa tarde')
    else:
       print('Ba noite')
else:
    print("digite um valor valido!")