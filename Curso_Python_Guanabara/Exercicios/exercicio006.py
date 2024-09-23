# Desafio 006 - Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada:


numero = float(input("Digite aqui um numero: "))
print(numero)

dobro = numero * 2
print(f"O dobro do numero digitado é: {dobro}")

triplo = numero * 3 
print(f"O triplo do numero digitado é: {triplo}")

raiz_quadrada = numero ** (1/2)         
print(f"A raiz quadrada do numero digitado é: {raiz_quadrada:.2f}")