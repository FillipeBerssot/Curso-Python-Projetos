# 16- Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

temperatura_celsius = float(input("Digite uma temperatura em Celsius: "))

temperatura_fahrenheit = 9 * temperatura_celsius 
temperatura_fahrenheit1 = temperatura_fahrenheit / 5 
temperatura_fahrenheit2 = temperatura_fahrenheit1 + 32 
temperatura_fahrenheit_arredondado = round(temperatura_fahrenheit2)


temperatura_fahrenheit01 = ((9 * temperatura_celsius)/5) + 32
print(temperatura_fahrenheit01)

print(f"A temperatura digitada convertida de Celsius para Fahrenheit será: {temperatura_fahrenheit_arredondado}ºF")