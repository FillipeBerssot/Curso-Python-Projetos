# Desafio 035- Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou nao formar um triangulo:

r1 = float(input('Digite aqui o valor da primeira reta para ver se forma um triangulo: '))
r2 = float(input('Digite aqui o valor de segunda reta para ver se forma um triangulo: '))
r3 = float(input('Digite aqui o valor de terceira reta para ver se forma um triangulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("SIM, PODE  FORMAR UM TRIANGULO")
else:
    print("NÃO, NÃO PODE FORMAR UM TRIANGULO")

