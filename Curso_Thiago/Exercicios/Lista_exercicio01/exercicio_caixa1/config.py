def verificacao_do_codigo_de_barra(codigo_de_barras, carrinho, flag=False):

    if codigo_de_barras == "0" and not carrinho:
        print("Não é possível prosseguir sem nada.")
    elif codigo_de_barras == "0" and carrinho:
        flag = True

    return flag


def criar_lista_de_compra(
    lista_de_mercadorias, codigo_de_barras, carrinho, quantidades, flag=False
):

    for mercadoria in lista_de_mercadorias:
        if mercadoria["codigo_de_barras"] == codigo_de_barras:
            if codigo_de_barras in quantidades:
                quantidades[codigo_de_barras] += 1
            else:
                carrinho.append(mercadoria)
                quantidades[codigo_de_barras] = 1
            print(
                f"Produto adicionado: {mercadoria['nome']} - R$ {mercadoria['preco'] / 100:.2f}"
            )
            flag = True

    if flag is False:
        print("Código de barras não encontrado. Tente novamente.")


import time


config = dict()


def configuracoes_gerais_do_projeto():

    config["taxa_tributo"] = 1.1517
    config["data_atual_formatada"] = time.strftime(
        "%d/%m/%Y %H:%M:%S", time.localtime()
    )

    return config