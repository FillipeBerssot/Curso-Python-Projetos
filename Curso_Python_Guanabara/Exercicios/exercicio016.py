# Desafio 016- Crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira:
# Ex: o numero 6.127 tem a parte inteira de 6.

import math

numero = float(input("Digite um numero decimal: "))
# print(numero)

numero_inteiro = math.trunc(numero)
numero_inteiro2 = round(numero)
print(f"A porção inteiro de {numero} é {numero_inteiro}")