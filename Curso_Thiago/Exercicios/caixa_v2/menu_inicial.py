from carrinho2 import criar_carrinho, calcular_preco_do_carrinho, exibir_resumo_carrinho    # --> Importa do modulo "carrinho2.py" as funções "criar_carrinho,
                                                                                            #      calcular_preco_do_carrinho, exibir_resumo_carrinho".

from pagamento import efetuar_pagamento                          #  --> Importa do modulo "pagamento.py" a função "efetuar_pagamento".

from cpf import inserir_cpf                                      # --> Importa do modulo "cpf.py" a função "inserir_cpf".

from impressao_nota_fiscal import imprimir_nota_fiscal           # --> Importa do modulo "impressao_nota_fiscal.py" a função "imprimir_nota_fiscal".

from desconto import calcular_desconto                           # --> Importa do modulo "desconto.py" a função "calcular_desconto".

from produtos import lista_de_mercadorias                        # ---> Importa do modulo "produtos.py" a "lista_de_mercadorias", onde contem os produtos salvos.


# Função "menu", foi criado para formatar um menu para o programa, onde utiliza uma estrutura de repetição "while True" para fazer com que as 
#   opções sejam inseridas no menu e utilizadas de forma correta, onde caso seja digitado algo errado recebe uma mensagem de erro, fazendo tambem
#   com que sempre volte ao menu inicial após o uso.
def menu():
    """
    Exibe o menu principal do sistema e processa a escolha do usuário.

    Opções:
        [1] Cadastrar uma nova compra.
        [2] Listar produtos.
        [3] Encerrar o programa.
    """
    while True:
        opcao = input('''
======================================================================================
                       .:PROJETO CAIXA REGISTRADORA v.2 PYTHON:.
                              .:SUPERMERCADO BOA COMPRA:.
======================================================================================
MENU:
      
[1] .:CADASTRAR UMA NOVA COMPRA:.
[2] .:EXIBIR LISTA DE PRODUTOS:.
[3] .:ENCERRAR O PROGRAMA.:
                  
ESCOLHA SUA OPÇÃO: ''').strip()

        if opcao == '1':
            cadastrar_nova_compra()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            encerrar_programa()
        else:
            print('Opção inválida. Por favor, tente novamente.')


# Função "cadastrar_nova_compra", foi criado para armazenar varias funções necessarias para o funcionamento do programa, onde irá cadastrar uma nova compra caso
#   o usuario desejar. 
# Função muito importante para o funcionamento do programa.
def cadastrar_nova_compra():
    """
    Processa a criação de uma nova compra, incluindo:

    - Adicionar produtos ao carrinho.
    - Aplicar descontos.
    - Calcular os valores do carrinho.
    - Efetuar o pagamento.
    - Inserir CPF.
    - Emitir a nota fiscal.
    """
    carrinho = criar_carrinho()
    calcular_desconto(carrinho["produtos"])
    calcular_preco_do_carrinho(carrinho)
    exibir_resumo_carrinho(carrinho)
    efetuar_pagamento(carrinho)
    cpf = inserir_cpf()
    imprimir_nota_fiscal(carrinho, cpf)


# Função "listar_produtos", foi criado para exibir ao usuario a lista de produtos ja salvas no programa, percorre o produto na "lista_de_mercadorias",
#   utilizando uma estrutura de repetição "for" e exibi os valores formatados para o usuario.
def listar_produtos():
    """
    Exibe a lista de produtos disponíveis no sistema, mostrando o código de barras,
    nome do produto e o preço formatado.
    """
    print("\nLista de Produtos Disponíveis:")
    for produto in lista_de_mercadorias:
        print(f"Código: {produto['codigo_de_barras']} - {produto['nome']} - R$ {produto['preco'] / 100:.2f}")


# Função "encerrar_programa", foi criado para encerrar o programa. Mostra ao usuario uma mensagem final de encerramento e agradecimento.
# Encerrando o programa a partir de uma função "exit()" que encerra o programa ou script que está em execução.
def encerrar_programa():
    """
    Utiliza a função "exit()" que encerra o programa ou script que está
    em execução.
    Exibindo uma mensagem de agradecimento e encerra o programa.
    """
    print("\nEncerrando o programa. Obrigado por usar o sistema do Supermercado Boa Compra!")
    exit()
