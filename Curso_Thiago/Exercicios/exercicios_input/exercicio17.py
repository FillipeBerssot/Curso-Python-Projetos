# 17- Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado:

kms_percorridos = float(input("Digite aqui a quantidade de kms percorridos no carro: "))
dias_utilizados = float(input("Digite aqui quantos dias foram alugados no carro: "))

custo_a_pagar_aluguel = dias_utilizados * 60
custo_a_pagar_kms = kms_percorridos * 0.15
custo_total_a_pagar = custo_a_pagar_aluguel + custo_a_pagar_kms

print(f"De acordo com os dados inseridos o valor total será de R$ {custo_total_a_pagar}")
