import time


from forma_de_pagamento import forma_de_pagamento
from produtos import lista_de_mercadorias
from config import configuracoes_gerais_do_projeto
from carrinho import verificacao_do_codigo_de_barra, criar_lista_de_compra
from resumo_da_compra import resumo_da_compra
from inserir_cpf import inserir_cpf

configuracoes = configuracoes_gerais_do_projeto()

while True:
    carrinho = []
    quantidades = {}
    print("Digite os códigos de barras dos produtos (digite '0' para finalizar):")

    while True:
        codigo_de_barras = input("Código de barras: ").strip()
        flag = verificacao_do_codigo_de_barra(codigo_de_barras=codigo_de_barras, carrinho=carrinho)
        
        if flag:
            break
        
        criar_lista_de_compra(lista_de_mercadorias=lista_de_mercadorias, 
                              codigo_de_barras=codigo_de_barras, 
                              quantidades=quantidades, 
                              carrinho=carrinho)
        
 
    compra = resumo_da_compra(carrinho, quantidades, configuracoes)

    forma_de_pagamento(compra)

    # Inserção do CPF na nota
    inserir_cpf()

    # Impressão da Nota Fiscal
    print("\nProcessando sua Nota Fiscal...")
    time.sleep(3)
    print(f"\n{'=' * 46} Nota Fiscal {'=' * 46}")
    print("-" * 105)
    print(
        f"{'Código':<10} {'Nome':<20} {'Qtd':<5} {'Valor Unit.':<12} {'Total':<12} {'Desconto':<10} {'Valor Desc.':<15} {'Valor Final':<12}"
    )
    print("-" * 105)

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

        print(
            f"{codigo_de_barras:<10} {nome:<20} {quantidade:<5} R$ {preco / 100:<10.2f} R$ {valor_total / 100:<10.2f} {desconto * 100:>6.2f}% R$ {valor_desconto / 100:<13.2f} R$ {valor_final / 100:<10.2f}"
        )

    print("-" * 105)
    print(f"Total da compra:{'_' * 80}R$ {compra["total"] / 100:.2f}")
    if compra["total_com_desconto"] < compra["total"]:
        print(
            f"Total da compra com desconto:{'_' * 65}R$ {compra["total_com_desconto"] / 100:.2f}"
        )
    print(f"Total da compra com tributos (15.7%):{'_' * 59}R$ {compra["total_com_tributo"]:.2f}")
    if cpf:
        print(f"CPF:{'_' * 87}{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    else:
        print("CPF: Não informado")
    print(f"Data e Hora:{'_' * 74}{configuracoes["data_atual_formatada"]}")
    print(f"Forma de Pagamento:{'_' * 69}{forma_pagamento}")

    print("-" * 105)
    print("-" * 105)
    print("-" * 105)

    print("Detalhamento do Desconto:")
    print(
        f"{'Código':<10} {'Nome':<20} {'Valor Unit.':<12} {'Total':<12} {'Desconto':<10} {'Valor Desc.':<15} {'Valor Final':<12}"
    )

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

        compra["total"] += valor_total
        compra["total_com_desconto"] += valor_final

        for c in range(quantidade):
            print(
                f"{codigo_de_barras:<10} {nome:<20} R$ {preco / 100:<10.2f} R$ {valor_total / 100:<10.2f} {desconto * 100:>6.2f}% R$ {valor_desconto / 100:<13.2f} R$ {valor_final / 100:<10.2f}"
            )

    total_com_tributo = compra["total_com_desconto"] * configuracoes["taxa_tributo"]

    print(f"\nTotal da compra (sem os descontos e tributos): R$ {compra["total"] / 100:.2f}")
    print(f"Total da compra com os descontos: R$ {compra["total_com_desconto"] / 100:.2f}")
    print(
        f"Total da compra com o desconto e os tributos (15.17%): R$ {total_com_tributo / 100:.2f}"
    )

    total_com_tributo = total_com_tributo / 100

    # Registrar uma nova compra:
    nova_compra = input("\nDeseja registrar uma nova compra? (s/n): ").strip().lower()
    if nova_compra != "s":
        print("Encerrando o sistema.")
        break
