# Ex.063- Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma,
# Sequencia de Fibonacci:
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)

numero = int(input("Digite o número de elementos que você quer ver da sequência de Fibonacci: "))

termo_1 = 0
termo_2 = 1
print('~' * 30)
print(f'{termo_1} --> {termo_2}', end='')
contador = 3

while contador <= numero:
    termo_3 = termo_1 + termo_2
    print(f' --> {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print(' --> FIM')
print('~' * 30)