# Desafio 010- Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar:

valor_reais = float(input("Quantos reais voçê tem na sua carteira nesse momento? "))
# print(valor_reais)

valor_dolar = valor_reais / 3.27
print(f"Convertendo o que voçê tem de reais para dolares, voçê teria {valor_dolar:.2f} dolares.")