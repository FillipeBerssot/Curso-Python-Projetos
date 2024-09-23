# Ex.047- Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50:

for c in range(1, 50+1):
    if c % 2 == 0:
        print(c)
print('FIM')
print('SOMENTE OS VALORES PARES')

for c in range(1, 50 + 1):
    if c % 2 != 0:
        print(c)
print('FIM')
print('SOMENTE OS VALORES IMPARES')
