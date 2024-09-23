# Desafio 008- Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros:

valor = (float(input("Digite aqui um valor aleatorio em metros: ")))
# print(valor)

centimetros = valor * 100
print(f'O valor em metros convertido para centimetros é: {centimetros}')

milimetros = valor * 1000
print(f"O valor em metros convertido para milimetros é: {milimetros}")