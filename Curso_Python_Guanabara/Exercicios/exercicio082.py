# Ex. 082- Crie um programa que vai ler varios numeros e colocar em uma lista:
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente:
# Ao final, mostre o conteudo das tres listas geradas:

num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite aqui um numero: ')))
    resp = input('Quer continuar?[s/n]: ').strip().lower()
    if resp in 'n':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print('-=' * 40)
print(f'Esses são os numeros dentro da sua lista: {num}')
print(f'Esses são os numeros pares na sua lista de numeros Pares: {pares}')
print(f'Esses são os numeros impares na sua lista de numeros Impares: {impares}')
