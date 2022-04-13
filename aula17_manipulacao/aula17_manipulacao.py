'''
Manipulação de Strings

 * Strings indices
 * Fatiamento de strings (inicio:fim:passo)
 * Funções built-n len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
'''

#positivos   [012345678]
texto =      'Python S2'
#negativos - [987654321]


nova_str = texto[2:6]
nova_str1 = texto[:6]
outra_str = texto[-2]
outraStr2 = texto[:-1]
outraStr22 = texto[-9:-3]
str_pula = texto[0:6:2]
print(nova_str)
print(nova_str1)
print(outra_str)
print(outraStr2)
print(outraStr22)
print(str_pula)
print(len(texto))

