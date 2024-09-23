# 14- Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar:

preco_mercadoria = float(input("Digite aqui o preço de uma mercadoria: "))
percentual_de_desconto = float(input("Digite agora a porcentagem de desconto: "))

preco_mercadoria_com_desconto = preco_mercadoria * (percentual_de_desconto / 100)
novo_preco_mercadoria = preco_mercadoria - preco_mercadoria_com_desconto

print(f"De acordo com os valores digitados o desconto na mercadoria será de R$: {preco_mercadoria_com_desconto} e o valor da mercadoria será de R$: {novo_preco_mercadoria}")