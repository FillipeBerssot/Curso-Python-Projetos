# VARIAVEIS COMPOSTAS :
#   LISTAS: [ ]
#       Podem ser mutaveis

num = [2 ,5, 9, 1]

num[2] = 3

num.append(7)

num.sort(reverse = True)

num.insert(2, 0)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')

num.pop(2)

print(num)
print(f'Essa lista tem {len(num)} elementos.')

# Exemplo 01:
valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):                              # enumerate == pegar valor e chave (c e v)
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei no final da lista.')

# Exemplo 02:
a = [2, 3, 4, 7]
b = a[:]                                                     # [:] == Criar uma copia da lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')