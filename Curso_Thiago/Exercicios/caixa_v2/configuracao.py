import time      # ---> O programa está importando a biblioteca "time" para utilizar de seus recursos durante o programa. Esta fazendo uma importação
                 #          completa da biblioteca.


# Função "configuracao_do_projeto", foi criado para armazenar dados necessarios que seram utilizados durante o programa. Os dados foram salvos em uma variavel chamada
#   "configuracoes" que está armazenando esses dados em um dicionario. 
# Essa função retorna essas "configuracoes" que será utilizada no programa em um dicionario.
def configuracao_do_projeto() -> dict:
    """
    Retorna as configurações necessárias para o funcionamento do projeto.

    As configurações incluem:
        - taxa_tributo (float): A taxa de tributo aplicada às compras.
        - taxa_tributo_porcentagem (str): A porcentagem do tributo exibida em formato legível.
        - data_formatada (str): A data e hora atuais no formato "dd/mm/yyyy hh:mm:ss".
        - formas_de_pagamento (dict): As opções de pagamento disponíveis (cartão de crédito, débito, Pix e dinheiro).   
    
    Retorna:
        dict: Um dicionário contendo as configurações.
    """
    configuracoes = {
        "taxa_tributo": 1.1517,
        "taxa_tributo_porcentagem": "15.17%",
        "data_formatada": time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()),
        "formas_de_pagamento": {
            "1": "Cartão de Crédito",
            "2": "Cartão de Débito",
            "3": "Pix",
            "4": "Dinheiro",
        },
    }
    return configuracoes
