# Ex.100- Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteio() e somaPar().
# A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar a soma
# entre todos os valores PARES sorteados pela função anterior:

from random import randint
from time import sleep


# Maneira 01:
def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 100)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {lista}, temos {soma}.')


valores = []
sorteio(valores)
somaPar(valores)

print('=' * 60)

# Maneira 02:
def sorteio02():
    numeros = []
    for v in range(1,6):
        numeros_aleatorios = randint(0,100)
        numeros.append(numeros_aleatorios)
    return numeros


def somaPar02(lista_de_numeros):
    soma = 0
    for numeros in lista_de_numeros:
        if numeros % 2 == 0:
            soma += numeros
    print(f'Somando os valores pares de {lista_de_numeros}, temos {soma}.')


numeros_sorteados = sorteio02()
print(f'Sorteando 5 valores da lista: {numeros_sorteados} PRONTO!')
somaPar02(numeros_sorteados)
