def resumo_da_compra(carrinho, quantidades, obter_desconto, taxa_do_tributo):
    """
    Mostra na nota fiscal o resumo de toda compra regidstrada.
    """
    total = 0
    total_com_desconto = 0

    print("\nResumo da Compra:")

    for item in carrinho:
        codigo_de_barras = item['codigo_de_barras']
        nome = item['nome']
        preco = item['preco']
        quantidade = quantidades[codigo_de_barras]

        # Calcular o desconto baseado na quantidade:
        # Usei a função obter_desconto
        desconto_produtos = obter_desconto(quantidade)
        # Continuar com os calculos necessarios:
        valor_total = preco * quantidade
        valor_desconto = valor_total * desconto_produtos
        valor_final = valor_total - valor_desconto

        total += valor_total
        total_com_desconto += valor_final

    total_com_tributo = total_com_desconto * taxa_do_tributo

    return(total_com_tributo, total, total_com_desconto)