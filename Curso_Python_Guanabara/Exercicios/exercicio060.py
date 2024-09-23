# Faça um programa que leia um numero qualquer e mostre o seu fatorial:
# Ex: 5 = 5x4x3x2x1 = 120.

# Primeira maneira com biblioteca:
from math import factorial
n = int(input('Digite aqui um numero para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial do numero {n} é: {f}.')

# Segunda maneira:
numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
contador = numero

print(f"Calculando o fatorial de {numero}:")
print(f"{numero}! = ", end="")

while contador > 0:
    print(f"{contador}", end="") 
    fatorial *= contador
    contador -= 1
    if contador > 0:
        print(" x ", end="") 
    else:
        print(" = ", end="") 

print(f"{fatorial}")
