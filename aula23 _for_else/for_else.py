'''

AULA23  FOR / ELSE - 06/04/22

'''

vari = ['Mateus ceni', 'dBalder', 'Gato']
#
# comeca_com_b = False
# for valor in vari:
#     if valor.lower().startswith('b'):
#        comeca_com_b = True
#
# if comeca_com_b:
#     print("tem uma palavra que começa com B")
# else:
#     print("não tem palavra q começa com B")

#ou


for valor in vari:
    print(valor)
    if valor.lower().startswith('b'):
        break
else:
    print("não tem palavra q começa com B")