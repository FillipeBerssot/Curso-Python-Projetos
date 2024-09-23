# Ex. 074- Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla:

import random

#Maneira 01:
numeros_aleatorios01  = random.randint(0,10)
numeros_aleatorios02  = random.randint(0,10)
numeros_aleatorios03  = random.randint(0,10)
numeros_aleatorios04  = random.randint(0,10)
numeros_aleatorios05  = random.randint(0,10)

tupla_de_5_numero = numeros_aleatorios01, numeros_aleatorios02, numeros_aleatorios03, numeros_aleatorios04, numeros_aleatorios05
print('Os valores gerados foram:', *tupla_de_5_numero)
print(f'O maior valor gerado foi: {max(tupla_de_5_numero)}')
print(f'O menor valor gerado foi: {min(tupla_de_5_numero)}')

#Maneira 02:
tupla_de_5_numeros = (
    random.randint(0,10),
    random.randint(0,10),
    random.randint(0,10),
    random.randint(0,10),
    random.randint(0,10)
) 
print(f'\nOs valores gerados foram: ', end='')
for n in tupla_de_5_numero:
    print(f'{n} ', end='')

print(f'\nO maior valor gerado foi: {max(tupla_de_5_numeros)}')
print(f'O menor valor gerado foi: {min(tupla_de_5_numeros)}')

