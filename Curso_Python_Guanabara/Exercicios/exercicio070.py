# Ex.070 - Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra: FEITO
# B) Quantos produtos custam mais de R$ 1000: FEITO
# C) Qual é o nome do produto mais barato: FEITO

# Opcao 01:
total = 0
totmil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = input('Nome do produto: ').strip().capitalize()
    preco = float(input('Preço R$: '))

    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? ').strip().upper()[0]

    if resp == 'N':
        break

print(f'FIM DO PROGRAMA')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')


# Opcao 02:  Usando Dicionario
'''lista_de_produtos_adicionados = {}

while True:
    nome_produto = input('Digite aqui o nome do produto comprado: ').strip().capitalize()
    preco_produto = float(input('Digite agora o preço do produto comprado R$: '))
    lista_de_produtos_adicionados[nome_produto] = preco_produto

    continuar = input('Deseja adicionar o nome e o preço de mais algum produto? [S / N]: ').strip().upper()

    if continuar == 'N':
        print('\nFinalizando o programa. Mostrando os dados das suas compras abaixo: ')

        total_gasto = 0
        produtos_acima_1000 = []
        quantidade_produtos_acima_1000 = 0
        item_mais_barato = None
        preco_mais_barato = float('inf')

        for produto in lista_de_produtos_adicionados:
            preco = lista_de_produtos_adicionados[produto]
            total_gasto +=preco

            if preco < preco_mais_barato:
                preco_mais_barato = preco
                item_mais_barato = produto

            if preco > 1000:
                quantidade_produtos_acima_1000 += 1
                produtos_acima_1000.append(produto)

        print(f'O total gasto na sua compra foi de R$: {total_gasto:.2f}')
        print(f'{quantidade_produtos_acima_1000} produto(s) comprados custaram mais de R$ 1.000')
        if quantidade_produtos_acima_1000 > 0:
            print(f'Os produtos acima de R$ 1.000 foram: {", ".join(produtos_acima_1000)}')

        if item_mais_barato:
            print(f'O item mais barato da sua compra foi: {item_mais_barato}, custando R$: {preco_mais_barato:.2f}')
        else:
            print("Nenhum produto foi adicionado.")
        break'''
