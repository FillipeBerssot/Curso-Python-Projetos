# Ex.085- Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica 
# que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente:

#Maneira 01:
numero = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor %2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('-=' * 30)

numero[0].sort()
numero[1].sort()

print(f'Todos os valores pares digitados foram: {numero[0]}')
print(f'Todos os valores impares digitados foram: {numero[1]}')

#Maneira 02:
valores = []
numeros_pares= []
numeros_impares = []

for v in range(1,8):
    numeros = int(input(f'Digite o {v}º valor: '))
    valores.append(numeros)
    if numeros % 2 == 0:
        numeros_pares.append(numeros)
        print('Numero par adicionado a lista de numeros pares.')
    elif numeros % 2 == 1:
        numeros_impares.append(numeros)
        print('Numero impar adicionado a lista de numeros impares.')

numeros_impares.sort()
numeros_pares.sort()

print(f'\nOs valores da sua lista são: {valores}')
print(f'Os valores Pares em ordem crescente são: {numeros_pares}')
print(f'Os valores Impares em ordem crescente são: {numeros_impares}')