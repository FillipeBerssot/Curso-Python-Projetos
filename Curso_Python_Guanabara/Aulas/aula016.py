# Variaveis Compostas 
#   Tuplas: ( )
#       As tuplas são imutaveis

# Exemplo 01:
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])

# Exemplo 02:
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
print('Comi pra caramba!')

# Exemplo 03:
print(sorted(lanche))                   # sorted == Deixa ORDENADO

# Exemplo 04:
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(c.count(5))                       # count == contador 
print(c.index(8))                       # index == Mostrar posição

# Exemplo 05:
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)                             # del == apagar da memoria
print(pessoa)