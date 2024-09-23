# Desafio 012- Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:

preco = float(input("Digite aqui o preço do produto desejado: "))
print(f"O preço do produto desejado é R$: {preco}")

desconto = preco * 5 / 100
print(f'5% de desconto te dará um desconto de R$: {desconto:.2f}')

novo_preco = preco - desconto
print(f"O valor do seu produto com 5% de desconto agora será R$: {novo_preco:.2f}")