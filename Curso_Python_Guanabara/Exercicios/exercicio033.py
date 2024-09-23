# Desafio 033- Faça um programa que leia três numeros e mostre qual e o maior e qual e o menor:

numero = float(input("Digite aqui algum numero: "))
numero2 = float(input("Digite aqui algum numero: "))       
numero3 = float(input("Digite aqui algum numero: "))

maior = max(numero, numero2, numero3)
menor = min(numero, numero2, numero3)

print(f"O maior numero dentre os 3 numeros digitado é: {maior} ")
print(f"O menor numero dentre os 3 numeros digitado é: {menor}")
