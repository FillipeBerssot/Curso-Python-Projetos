from produtos import lista_de_mercadorias            # ---> Importa do modulo "produtos.py" a "lista_de_mercadorias", onde contem os produtos salvos.

from configuracao import configuracao_do_projeto     # ---> Importa do modulo "configuracao.py" a função "configuracao_do_projeto" onde está retornando a 
                                                     #        taxa_de_tributo, data_formatada e formas_de_pagamento, todos eles salvos em um formato de dicionario.


configuracoes = configuracao_do_projeto()            # ---> Está salvando o retorno da função "configuracao_do_projeto" em uma variavel chamada "configuracoes" 
                                                     #        para ser utilizada mais tarde dentro do código.

taxa_tributo = configuracoes["taxa_tributo"]         # ---> Está aproveitando a variavel "configuracoes" que armazena a função "configuracao_do_projeto" para 
                                                     #        armazenar e retornar quando for chamada somente a "taxa_tributo".


# Função "criar_carrinho", foi criado uma variavel chamada "carrinho" onde ela está armazenando um dicionario com varias chaves e valores para serem utilizadas 
#   com mais facilidade durante o codigo.
def criar_carrinho():
    """
    Cria um carrinho de compras com todos os dados necessários para a compra.

    O carrinho inclui os seguintes campos:
        - valor_total: O valor total dos produtos sem descontos e tributos.
        - valor_total_do_desconto: O total de descontos aplicados aos produtos.
        - valor_final: O valor final da compra após descontos.
        - valor_final_com_tributos: O valor final após a aplicação dos tributos.
        - produtos: Uma lista de produtos adicionados ao carrinho.
        - dados_de_pagamentos: Um dicionário com as informações de pagamento.   
    
    Retorna:
        Um dicionário representando o carrinho de compras.
    """
    carrinho = {
        "valor_total": 0,
        "valor_total_do_desconto": 0,
        "valor_final": 0,
        "valor_final_com_tributos": 0,
        "produtos": list(),
        "dados_de_pagamentos": {
            "dinheiro_recebido": 0,
            "troco": 0,
            "forma_de_pagamento": None 
        },
    }


    # Foi criado um Loop para que o usuario digitasse o codigo de barras do produto desejado, onde se utiliza um "for" para percorrer toda a "lista_de_mercadorias",
    #   para saber se realmente o codigo de barras digitado existe, sendo assim adicionando o produto ao dicionario "carrinho['produtos']" pela primeira vez e tambem
    #   adicionando o mesmo produto caso tenha sido adicionado mais de uma vez. Essa função tambem faz a verificação caso o usuario digite o codigo de barras errado ou
    #   tente dar continuidade ao programa sem nenhum produto adicionado ao carrinho. 
    # Essa função retorna o dicionario "carrinho" que será utilizada mais tarde nesse código.
    while True:
        codigo_de_barras = input("\nDigite o código de barras do produto (digite 0 para finalizar): ").strip()
        item_encontrado = False

        for mercadoria in lista_de_mercadorias:
            if (
                mercadoria["codigo_de_barras"] == codigo_de_barras
                and mercadoria not in carrinho["produtos"]
            ):
                item_encontrado = True
                mercadoria["quantidade"] = 1
                carrinho["produtos"].append(mercadoria)
            elif (
                mercadoria["codigo_de_barras"] == codigo_de_barras
                and mercadoria in carrinho["produtos"]
            ):
                item_encontrado = True
                mercadoria["quantidade"] += 1

        if item_encontrado is False and codigo_de_barras != "0":
            print(
                "Código de barras inexistente. Por favor, digite um código de barras existente."
            )

        if codigo_de_barras == "0":
            if not carrinho['produtos']:
                print("Por favor, adicione pelo menos um produto ao carrinho antes de finalizar.")
            else:
                break

    return carrinho


# Função "calcular_preco_do_carrinho", foi criado para percorrer o dicionario "carrinho["produtos"]", onde com os dados proporcionados faz os calculos necessarios
#   para dar continuidade ao programa, calculos esses salvos em uma lista dentro do dicionario "carrinho" chamado "carrinho["produtos"]", facilitando assim o uso
#   desses calculos para o sucesso do programa. 
# Utilizando de parametro o "carrinho" para assim obter os dados necessarios para fazer os calculos futuros.
def calcular_preco_do_carrinho(carrinho):
    """
    Percorre a lista "carrinho["produtos"] para realizar todos
    os calculos necessarios para a continuidade do programa.

    Adicionando itens necessarios a está lista.
    """
    for item in carrinho["produtos"]:
        item["valor_total"] = item["preco"] * item["quantidade"]
        item["desconto_total"] = item["valor_total"] * item["porc_de_desconto"]
        item["valor_final"] = item["valor_total"] - item["desconto_total"]
        item["valor_final_com_tributos"] = item["valor_final"] * taxa_tributo
        carrinho["valor_total"] += item["valor_total"]
        carrinho["valor_total_do_desconto"] += item["desconto_total"]
        carrinho["valor_final"] += item["valor_final"]

    carrinho["valor_final_com_tributos"] = (
        carrinho["valor_final"]  * configuracoes["taxa_tributo"]
    )


# Função "exibir_resumo_carrinho", foi criado para exibir os prints com os calculos necessarios para a visualização do usuario. 
# Essa função utiliza o parametro "carrinho" para poder exibir os dados em prints com maior clareza.
def exibir_resumo_carrinho(carrinho):
    """
    Exibe um resumo dos valores calculados do carrinho, como:
        - Total da compra sem descontos e tributos.
        - Total dos descontos aplicados.
        - Total final com descontos e tributos.
        
    Parâmetros:
        carrinho (dict): O carrinho de compras com os valores calculados.  
    """
    print(f"Total da compra (sem os descontos e tributos): R$ {carrinho["valor_total"] / 100:.2f}")
    print(f"Total dos descontos: R$ {carrinho["valor_total_do_desconto"] / 100:.2f}")
    print(
        f"Total da compra com os descontos e os tributos ({configuracoes["taxa_tributo_porcentagem"]}): R$ {carrinho["valor_final_com_tributos"] / 100:.2f}"
    )
