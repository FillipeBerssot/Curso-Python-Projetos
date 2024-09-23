# Desafio 017- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa:

import math


cateto_oposto = float(input("Digite o comprimento do cateto oposto de um triangulo retangulo: "))

cateto_adjacente = float(input("Digite o compriemnto do cateto adjacente de um triangulo retangulo: "))

soma_catetos = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
print(f"A soma dos quadrados das medidas dos catetos é {soma_catetos}")

hipotenusa = math.sqrt(soma_catetos)      # ou hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)   # ou hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f"O comprimento da hipotenusa é igual a soma dos catetos ao quadrado: {hipotenusa:.2f}")
