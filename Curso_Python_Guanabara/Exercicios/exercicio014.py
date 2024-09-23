# Desafio 014- Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para Fahrenheit:

celsius = float(input("Digite aqui uma temperatura em graus Celsius: "))
# print(celsius)

conversao = ((celsius * 9) / 5) + 32

print(f"A temperatura digitada de {celsius}° Celsius convertido para Fahrenheit será {conversao}° Fahrenheit.")