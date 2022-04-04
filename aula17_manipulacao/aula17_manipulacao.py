'''
Manipulação de Strings

 * Strings indices
 * Fatiamento de strings (inicio:fim:passo)
 * Funções built-n len, abs, type, preint, etc...
Essas funções podem ser usadas diretamente em cada tipo.
'''

#positivos   [012345678]
texto =      'Python S2'
#negativos - [987654321]


nova_str = texto[2:6]
outra_str = texto[-2]
outraStr2 = texto[:-1]
str_pula = texto[0:6:2]
print(nova_str)
print(outra_str)
print(outraStr2)
print(str_pula)
print(len(texto))

