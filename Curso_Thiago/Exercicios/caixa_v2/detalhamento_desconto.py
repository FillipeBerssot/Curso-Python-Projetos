# Função "detalhamento_desconto", foi criado para exibir a função "cabecario" e tambem para exibir os itens que estão armazenados dentro 
#   do "carrinho["produtos"]". 
# Utiliza o parametro "carrinho" para poder ter acesso a esses itens.
def detalhamento_desconto(carrinho):
    """
    Exibe o cabeçalho e os produtos armazenados no carrinho.

    Parâmetros:
        carrinho (dict): O carrinho contendo os produtos para exibição.
    """
    cabecario()
    detalhamento_produto(carrinho["produtos"])


# Função "cabecario", foi criado para exibir varios prints formatos dentro do programa, tambem exibe o "Detalhamento do Desconto" com as formatações corretas.
def cabecario():
    """
    Exibe o cabeçalho formatado para o detalhamento do desconto, mostrando as colunas
    de código, nome, quantidade, valor unitário, total, desconto e valor final.
    """
    print("-" * 105)
    print("-" * 105)
    print("-" * 105)

    print("Detalhamento dos Descontos:")
    print(
        f"{'Código':<10} {'Nome':<20} {'Qtd':<5} {'Valor Unit.':<12} {'Total':<12} {'Desconto':<10} {'Valor Desc.':<15} {'Valor Final':<12}"
    )


# Função "detalhamento_produto", foi criado para percorrer o produto dentro dos "produtos" utilizando um "for", onde tambem utiliza uma estrutura de 
#    repetição "while" para fazer os calculos necessarios dos itens em "produtos" para depois exibi-los de forma formatada para o usuario. Exibe tambem
#    um print finalizando e agradecendo o usuario pela compra.
# Essa função utiliza o parametro "produtos" para poder exibir os dados. 
def detalhamento_produto(produtos):
    """
    Percorre a lista de produtos, calcula os valores de desconto e formata os dados para exibição.

    Para cada produto, calcula o desconto e o valor final, exibindo-os em formato tabular.
    
    Após a exibição, uma mensagem de finalização da compra é mostrada.

    Parâmetros:
        produtos (list): A lista de produtos que será processada e exibida.
    """
    for produto in produtos:
        i = 0
        while i < produto["quantidade"]:
            valor_desconto = produto["preco"] * produto["porc_de_desconto"]
            valor_final = produto["preco"] - valor_desconto
            print(
            f"{produto["codigo_de_barras"]:<10} {produto["nome"]:<20} {1:<5} R$ {produto["preco"] / 100:<10.2f} R$ {produto["preco"] / 100:<10.2f} {produto["porc_de_desconto"] * 100:>6.2f}% R$ {valor_desconto / 100:<13.2f} R$ {valor_final / 100:<10.2f}"
        )
            i+=1
    print('\nCompra finalizada com sucesso. O Supermercado Boa Compra agradece a preferencia, volte sempre!')
