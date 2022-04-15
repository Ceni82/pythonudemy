'''
EXERCICIO 2
'''
# MEU COD DEU 'OK'!
# hora = input('Q horas são? ')
# hora = int(hora)
# if hora >= 0 and hora <= 11:
#     print('Bom dia!')
# elif hora >= 12 and hora <= 17:
#     print('Boa tarde!')
# elif hora <= 23:
#     print('Boa Noite!')
# else:
#     print('Hora invalida!')

# RESOLUÇÃO:

hora = input(' Digite um horario enttre 0 e 23: ')
if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
         print ('Horario deve estar entre 0 e 23!')
    else:
          if hora <= 11:
             print('Bom dia!')
          elif hora <= 17:
             print('Boa Tarde!')
          else:
             print ('Boa Noite!')
else:
    print('Horario deve estar entre 0 e 23!')