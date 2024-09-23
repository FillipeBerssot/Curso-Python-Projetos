# Função "calcular_desconto", foi criado para percorrer os itens dentro de "produtos" e fazer os calculos de desconto do programa.
# Utiliza estruturas condicionais para definir as porcentagens de desconto de acordo com as quantidades. 
# Essa função uitiliza de parametro os "produtos".
def calcular_desconto(produtos):
    """
    Aplica os descontos aos produtos com base na quantidade.

    Regras de desconto:
        - 20% de desconto para 10 ou mais produtos.
        - 15% de desconto para 5 a 9 produtos.
        - 10% de desconto para 3 a 4 produtos.
    
    Parâmetros:
        produtos (list): Uma lista de produtos, onde cada produto é um dicionário contendo a quantidade.
    """
    for item in produtos:
        item["porc_de_desconto"] = 0
        if item["quantidade"] >= 10:
            item["porc_de_desconto"] = 0.2
        elif 10 > item["quantidade"] >= 5:
            item["porc_de_desconto"] = 0.15
        elif 5 > item["quantidade"] >= 3:
            item["porc_de_desconto"] = 0.1
