def resumo_da_compra(carrinho, quantidades, configuracoes):
    total = 0
    total_com_desconto = 0
    total_com_tributo = 0

    print("\nResumo da Compra:")

    for item in carrinho:
        codigo_de_barras = item["codigo_de_barras"]
        nome = item["nome"]
        preco = item["preco"]
        quantidade = quantidades[codigo_de_barras]

        if quantidade >= 10:
            desconto = 0.20
        elif quantidade >= 5:
            desconto = 0.15
        elif quantidade >= 3:
            desconto = 0.10
        else:
            desconto = 0.00

        valor_total = preco * quantidade
        valor_desconto = valor_total * desconto
        valor_final = valor_total - valor_desconto

        total += valor_total
        total_com_desconto += valor_final

    total_com_tributo = total_com_desconto * configuracoes["taxa_tributo"]

    print(f"Total da compra (sem os descontos e tributos): R$ {total / 100:.2f}")
    print(f"Total da compra com os descontos: R$ {total_com_desconto / 100:.2f}")
    print(
        f"Total da compra com o desconto e os tributos (15.17%): R$ {total_com_tributo / 100:.2f}"
    )

    total_com_tributo = total_com_tributo / 100

    dados = {
        "total": total,
        "total_com_desconto": total_com_desconto,
        "total_com_tributo": total_com_tributo,
    }

    return dados