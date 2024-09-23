# Desafio 031- Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando
# R$ 0,50 por Km para viagens de ate 200 Km e R$ 0.45 para viagens mais longas:

distancia = float(input("Digite aqui a distancia da viagem em km : "))

if distancia <= 200:
    preco = distancia * 0.50
    print(f"O preço dessa viagem será: R${preco}")
else:
    preco = distancia * 0.45
    print(f"O preço dessa viagem será: R${preco}")
