# Ex. 084- Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas: FEITO
# B) Uma listagem com as pessoas mais pesadas: FEITO
# C) uma listagem com as pessoas mais leves: FEITO

#Maneira 02:
temporario = []
principal = []
maior = menor = 0
while True:
    temporario.append(input('Nome: '))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior == menor == temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
        principal.append(temporario[:])
        temporario.clear()
        resposta = input('Quer continuar?[S / N]: ')
        if resposta in 'Nn':
            break
print('-=' * 30)
print(f'Ao todo voçê cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior} kgs. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor} kgs. Peso de ', end='') 
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()

#Maneira 02:
pessoas = []
pessoas_pesadas = []
pessoas_leves = []

while True:
    nome = input('Nome: ').capitalize()
    peso = float(input('Peso: '))

    pessoas.append([nome, peso])

    if peso >= 100:
        pessoas_pesadas.append([nome, peso])
    elif peso <= 70:
        pessoas_leves.append([nome, peso])

    opcao = input('Deseja continuar? [s / n]: ').strip().lower()
    if opcao == 'n':
        break

# A):
print(f'O total de pessoas cadastradas foram: {len(pessoas)}')

# B) e C):
if pessoas_pesadas:
    print('\nA lista com as pessoas mais pesadas (>= 100 kg) são: ')
    for p in pessoas_pesadas:
        print(f'{p[0]} com {p[1]} kgs.')
else:
    print('Não há pessoas com peso >= 100 kgs')
if pessoas_leves:
    print('\nA lista com as pessoas mais leves (<= 70 kgs) são: ')
    for p in pessoas_leves:
        print(f'{p[0]} com {p[1]} kgs.')
else:
    print('Não há pessoas com peso <= 70 kgs.')