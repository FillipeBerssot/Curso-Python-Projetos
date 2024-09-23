# Desafio 015- Escreva um programa que pergunte a quantidade em Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por Km rodado:

km = float(input("Qual a quantidade de Kms rodados no carro: "))
# print(km)

dias = float(input("Por quantos dias o carro foi alugado: "))
# print(dias)

custo_dia = dias * 60
# print(custo_dia)

custo_km = km * 0.15
# print(custo_km)

custo_total = custo_dia + custo_km
print(f"De acordo com os kms rodados no carro que foram de {km} kms e os dias utilizados que foram de {dias:.0f} dias. Voçê terá que pagar um total de R$ {custo_total:.2f}.")