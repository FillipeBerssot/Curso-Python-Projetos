#Ex.24- Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit,
# e que, a partir da resposta do usuário, faça a devida conversão:

print("Conversor de Fahrenheit para Celsiu ou Celsius para Fahrenheit:")

print("Para qual temperatura voçê quer converter?")
print("Digite 1 para converter de Fahrenheit para Celsius: ")
print("Digite 2 para converter de Celsius para Fahrenheit: ")
conversao_temperatura = input(" ")

if conversao_temperatura == "1":
    temperatura = float(input("Digite agora a temperatura que será convertida: "))
    temperatura_convertida = (temperatura - 32) * (5/9)
    temperatura_convertida = round(temperatura_convertida, 2)
    print(f"{temperatura}° Fahrenheit convertido para Celsius será: {temperatura_convertida}° Celsius.")
elif conversao_temperatura == "2":
    temperatura = float(input("Digite agora a temperatura que será convertida: "))
    temperatura_convertida = (temperatura * (9 / 5)) + 32
    temperatura_convertida = round(temperatura_convertida, 2)
    print(f"{temperatura}° Celsius convertido para Fahrenheit será: {temperatura_convertida}° Fahrenheit.")