'''
revisao for in 05/04
'''

# txt = 'Python'
# for n, letra in enumerate(txt):
#     print(n, letra)

# for numero in range(20, 10, -1):
# #     print(numero)
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)


txt = 'Python'
new_str = ''

for letra in txt:
    if letra == 't':
        new_str += letra.upper()
    elif letra == 'h':
        new_str += letra.upper()
        break
    else:
        new_str += letra
print (new_str)