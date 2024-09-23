import time

def impressao_da_nota_fiscal(dados_compra):
    """
    Verifica os dados usados durante a compra e formata-os em uma Nota Fiscal.
    Nota Fiscal contém todos os dados usados porem:
    Caso nao seja recebido um cpf ele irá informar na Nota Fiscal (CPF_Nao informado).
    Caso não tenha descontos na compra ele não irá informar o total_com_desconto na Nota Fiscal.
    """
    print('\nProcessando sua Nota Fiscal...')
    time.sleep(3)
    print(f"\n{'=' * 46} Nota Fiscal {'=' * 46}")
    print("-" * 105)
    print(f"{'Código':<10} {'Nome':<20} {'Qtd':<5} {'Valor Unit.':<12} {'Total':<12} {'Desconto':<10} {'Valor Desc.':<15} {'Valor Final':<12}")
    print("-" * 105)

    # Extrair dados do dicionário
    carrinho = dados_compra['carrinho']
    quantidades = dados_compra['quantidades']
    total = dados_compra['total']
    total_com_desconto = dados_compra['total_com_desconto']
    total_com_tributo = dados_compra['total_com_tributo']
    cpf = dados_compra['cpf']
    data_hora_atualizado = dados_compra['data_hora']
    forma_pagamento = dados_compra['forma_pagamento']
    obter_desconto = dados_compra['obter_descontos']

    for item in carrinho:
        codigo_de_barras = item['codigo_de_barras']
        nome = item['nome']
        preco = item['preco']
        quantidade = quantidades[codigo_de_barras]

        # Calcular desconto
        desconto_produtos = obter_desconto(quantidade)
        valor_total = preco * quantidade
        valor_desconto = valor_total * desconto_produtos
        valor_final = valor_total - valor_desconto

        print(f"{codigo_de_barras:<10} {nome:<20} {quantidade:<5} R$ {preco / 100:<10.2f} R$ {valor_total / 100:<10.2f} {desconto_produtos * 100:>6.2f}% R$ {valor_desconto / 100:<13.2f} R$ {valor_final / 100:<10.2f}")

    print("-" * 105)
    print(f"Total da compra:{'_' * 80}R$ {total / 100:.2f}")
    if total_com_desconto < total:
        print(f"Total da compra com desconto:{'_' * 65}R$ {total_com_desconto / 100:.2f}")
    print(f"Total da compra com tributos (15.7%):{'_' * 59}R$ {total_com_tributo:.2f}")
    if cpf:
        print(f"CPF:{'_' * 87}{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    else:
        print(f'CPF:{'_'*87}Não informado')
    print(f"Data e Hora:{'_' * 74}{data_hora_atualizado}")
    print(f"Forma de Pagamento:{'_' * 69}{forma_pagamento}")

    print('-' * 105)

