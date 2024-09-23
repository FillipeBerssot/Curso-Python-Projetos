# 02- Escreva um programa que leia um valor em metros e o exiba convertido em milímetros:                 #se o usuario digitar "30 metros"

valor_metros = int(input("Digite aqui algum valor em metros: "))
print(f"{valor_metros} metros")

valor_em_mm = valor_metros / 0.001
print(f"O valor digitado de {valor_metros} metros, convertido para milimetros é de: {valor_em_mm} milimetros.")
