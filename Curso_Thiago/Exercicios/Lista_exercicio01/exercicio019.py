# Ex. 019- Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

i = int(input('Digite um numero inteiro que quer obter o fatorial: '))
lista = list(range(1, i+1))

produto = 1
for numero in lista:
    produto = numero * produto

print(produto)