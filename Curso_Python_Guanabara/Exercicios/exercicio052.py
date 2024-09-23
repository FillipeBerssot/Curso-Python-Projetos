# Ex.052- Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo:

numero = int(input('Digite aqui um numero e descubra se é ou não primo: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO numero {numero} foi divisivel {total} vezes.')
if total == 2:
    print('E por isso ele É PRIMO.')
else:
    print('E por isso ele NÂO É PRIMO.')
