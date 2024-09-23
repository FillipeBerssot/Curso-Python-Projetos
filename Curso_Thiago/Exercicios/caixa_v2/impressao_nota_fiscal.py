import time                # ---> O programa está importando a biblioteca "time" para utilizar de seus recursos durante o programa. Esta fazendo uma importação
                           #          completa da biblioteca.

from configuracao import configuracao_do_projeto      # ---> Importa do modulo "configuracao.py" a função "configuracao_do_projeto" onde está retornando a 
                                                      #        taxa_de_tributo, data_formatada e formas_de_pagamento, todos eles salvos em um formato de dicionario.

from detalhamento_desconto import detalhamento_desconto     # ---> Importa do modulo "detalhamento_desconto.py" a função "detalhamento_desconto" onde está retornando 
                                                            #          o cabecario formatado e os itens armazenados do "carrinho["produtos"]".
                                                        

configuracao = configuracao_do_projeto()             # ---> Está salvando o retorno da função "configuracao_do_projeto" em uma variavel chamada "configuracao" 
                                                     #        para ser utilizada mais tarde dentro do programa.


# Função "imprimir_nota_fiscal", foi criado para inicializar nota fiscal com a função "inicializando_nota", mostrar o cabecario com a função
#   "cabecario", detalha todos os itens armazenados pela função "detalhamento_produto", mostra o rodape formatado pela função "rodape".
# Recebe os parametros para o funcionamento "carrinho" e "cpf".
def imprimir_nota_fiscal(carrinho, cpf):
    """
    Imprime a nota fiscal com todos os detalhes.

    Exibe o cabeçalho, os produtos, o rodapé com o total da compra, o desconto e o tributo.
    Também exibe o CPF, se informado.

    Parâmetros:
        carrinho (dict): O carrinho de compras contendo os produtos.
        cpf (str): O CPF informado pelo usuário ou "Não informado".
    """
    inicializando_nota()
    cabecario()
    detalhamento_produto(carrinho["produtos"])
    rodape(carrinho, configuracao["data_formatada"], cpf)
    detalhamento_desconto(carrinho)


# Função "inicializando_nota", foi criado para receber da biblioteca "time" a funcionalidade "sleep", onde ela faz com que a Nota Fiscal apareça após 3 segundos.
def inicializando_nota():
    """
    Utiliza a funcionalidade "sleep" para fazer com que a Nota fiscal
    leve 3 segundos para aparecer para o usuario.
    """
    print("\nProcessando a sua Nota Fiscal. Por favor, aguarde um momento...")
    time.sleep(3)


# Função "cabecario", foi criado para receber todos os valores necessarios para registrar a Nota fiscal e tambem recebendo os valores necessarios para
#   ficar todos os valores formatados da forma mais parecida de uma Nota fiscal real.
def cabecario():
    """
    Exibe o cabeçalho formatado da nota fiscal, incluindo as colunas:
    Código, Nome, Quantidade, Valor Unitário, Total, Desconto, Valor com Desconto e Valor Final.
    """
    print(f"\n{'=' * 46} Nota Fiscal {'=' * 46}")
    print("-" * 105)
    print(
        f"{'Código':<10} {'Nome':<20} {'Qtd':<5} {'Valor Unit.':<12} {'Total':<12} {'Desconto':<10} {'Valor Desc.':<15} {'Valor Final':<12}"
    )
    print("-" * 105)


# Função "detalhamento_produto", foi criado para percorrer o produto dentro dos produtos e mostrar os valores necessarios e formatados para a Nota fiscal.
# Recebe de parametros os "produtos" para poder ter acesso aos valores necessarios para a criação da Nota Fiscal.
def detalhamento_produto(produtos):
    """
    Percorre a lista de produtos e imprime seus detalhes na nota fiscal.

    Parâmetros:
        produtos (list): Lista de produtos contendo os dados necessários para exibição.
    """
    for produto in produtos:
        print(
        f"{produto["codigo_de_barras"]:<10} {produto["nome"]:<20} {produto["quantidade"]:<5} R$ {produto["preco"] / 100:<10.2f} R$ {produto["valor_total"] / 100:<10.2f} {produto["porc_de_desconto"] * 100:>6.2f}% R$ {produto["desconto_total"] / 100:<13.2f} R$ {produto["valor_final"] / 100:<10.2f}"
    )


# Função "rodape", foi criado para exibir os valores principais da Nota fiscal e do carrinho para o usuario, ja utilizando os valores com suas formatações
#   necessarias. 
# Recebe de parametro o "carrinho, data_formatada, cpf" para poder acessar os valores e dar continuidade a Nota fiscal.
def rodape(carrinho, data_formatada, cpf):
    """
    Exibe o rodapé da nota fiscal, incluindo o total da compra, o desconto, o tributo e o CPF.

    Parâmetros:
        carrinho (dict): O carrinho de compras contendo os produtos.
        data_formatada (str): A data e hora da compra.
        cpf (str): O CPF do cliente ou "Não informado".
    """
    print("-" * 105)
    print(f"Total da compra:{'_' * 80}R$ {carrinho["valor_total"] / 100:.2f}")

    print(
        f"Total da compra com desconto:{'_' * 65}R$ {carrinho["valor_final"] / 100:.2f}"
    )
    print(f"Total da compra com tributos (15.7%):{'_' * 59}R$ {carrinho["valor_final_com_tributos"]/100:.2f}")

    print(f"Data e Hora:{'_' * 74}{data_formatada}")
    print(f"Forma de Pagamento:{'_' * 69}{carrinho["dados_de_pagamentos"]["forma_de_pagamento"]}")

    exibir_cpf(cpf)


# Função "exibir_cpf", foi criado para exibir o cpf inserido pelo usuario na Nota fiscal, utilizando uma estrutura condicional "if, else" para dar continuidade.
#   Caso o cpf seja informado ele ira formatar o cpf inserido de modo que apareça formatado (000.000.000-00) na Nota fiscal. 
#   Caso o cpf não seja informado ele ira formatar a Nota fiscal recebendo o valor de "Não Informado".
# Recebe o parametro "cpf" para poder acessar o valor armazenado para dar continuidade ao programa.
def exibir_cpf(cpf):
    """
    Exibe o CPF na nota fiscal. Se o CPF foi informado, ele é formatado.
    Formatado (000.000.000-00)
    Caso contrário, exibe "Não informado".

    Parâmetros:
        cpf (str): O CPF informado pelo usuário ou "Não informado".
    """
    if cpf and cpf != "Não Informado":
        print(f"CPF:{'_' * 87}{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    else:
        print(f"CPF:{'_' * 88}Não Informado")
