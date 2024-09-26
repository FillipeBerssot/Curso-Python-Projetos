# Ex. 016- Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares:

i = 0
lista_pares = []
lista_impares = []

while i < 10:
    numero = int(input('digite um numero inteiro: '))

    if numero % 2 == 0:
        lista_pares.append(i)
    elif numero % 2 != 0:
        lista_impares.append(i)
    i += 1

print(f'A quantidade de numeros pares é {len(lista_pares)}')
print(f'A quantidade de numeros impares é {len(lista_impares)}')
