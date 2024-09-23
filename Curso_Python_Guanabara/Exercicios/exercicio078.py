# Ex.078- Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista:

lista_numeros = []
maior_numero = 0
menor_numero = 0

for contador in range(0,5):
    lista_numeros.append(int(input(f'Digite um valor para a posição {contador}º: ')))
    if contador == 0:
        maior_numero = menor_numero = lista_numeros[contador]
    else:
        if lista_numeros[contador] > maior_numero:
            maior_numero = lista_numeros[contador]
        if lista_numeros[contador] < menor_numero:
            menor_numero = lista_numeros[contador]

print('=-' * 30)
print(f'Voce digitou os valores: {lista_numeros}')
print(f'O maior valor digitado foi o {maior_numero} nas posições:')
for indice, valor in enumerate(lista_numeros):
    if valor == maior_numero:
        print(f'{indice}... ', end='')
print()
print(f'O menor valor digitado foi o {menor_numero} nas posicões:')
for indice, valor in enumerate(lista_numeros):
    if valor == menor_numero:
        print(f'{indice}... ', end='')
print()
