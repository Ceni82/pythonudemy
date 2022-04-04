''' revisao - input'''

nome = input('Qual teu nome? ')
idade = input('Quantos anos vc tem? ')

ano_nascimento = 2022 - int(idade) #isso é um cast (int) é a conversao de um tipo
# de dado, no caso uma str para uma int

print (f' O nome da pessoa é {nome}, ele tem {idade} anos, ele nasceu em {ano_nascimento} e o tipo de dados são um {type(nome)}.')
