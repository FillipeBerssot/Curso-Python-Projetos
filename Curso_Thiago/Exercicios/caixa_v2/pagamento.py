import random               # ---> O programa está importando a biblioteca "random" para utilizar de seus recursos durante o programa. Esta fazendo uma importação
                            #         completa da biblioteca.

import time                 # ---> O programa está importando a biblioteca "time" para utilizar de seus recursos durante o programa. Esta fazendo uma importação
                            #         completa da biblioteca.

import qrcode_terminal     # ---> O programa está importando a biblioteca "qrcode_terminal" para utilizar de seus recursos durante o programa. Esta fazendo uma importação
                           #         completa da biblioteca.

import qrcode              # ---> O programa está importando a biblioteca "qrcode" para utilizar de seus recursos durante o programa. Esta fazendo uma importação
                           #         completa da biblioteca.

from configuracao import configuracao_do_projeto       # ---> Importa do modulo "configuracao.py" a função "configuracao_do_projeto" onde está retornando a 
                                                       #        taxa_de_tributo, data_formatada e formas_de_pagamento, todos eles salvos em um formato de dicionario.

configuracoes = configuracao_do_projeto()              # ---> Está salvando o retorno da função "configuracao_do_projeto" em uma variavel chamada "configuracao" 
                                                       #        para ser utilizada mais tarde dentro do programa.

opcoes_de_pagamento = configuracoes["formas_de_pagamento"]      # ---> Está aproveitando a variavel "configuracoes" que armazena a função "configuracao_do_projeto" para 
                                                                #        armazenar e retornar quando for chamada somente as "formas_de_pagamento".


# Função "efetuar_pagamento", foi criado para receber do usuario a forma em que ele deseja efetuar o pagamento da compra, no caso podendo pagar com 4 opções diferentes
#   sendo elas "Cartão de Crédito, Cartão de Débito, PIX, Dinheiro". Utilizando uma estrutura de repetição "while True" para receber os dados inseridos, validando os dados
#   para que sejam usados da forma correta dentro do programa, caso não seja, retorne para as opcões iniciais, tambem utiliza a estrutra condicional "if" para 
#   dar continuidade ao programa de acordo com a escolha do usuario.
# Recebe o parametro "carrinho" para acessar os valores necessarios para dar continuidade ao programa.
def efetuar_pagamento(carrinho):
    """
    Processa a escolha da forma de pagamento e executa o pagamento conforme a opção escolhida.

    Parâmetros:
        carrinho (dict): O carrinho de compras contendo os produtos e os valores finais.
    """
    while True:
        opcao_de_pagamento = input(
            "\nEscolha a forma de pagamento (1- Cartão de Crédito, 2- Cartão de Débito, 3- PIX, 4- Dinheiro): "
        ).strip()

        opcao_de_pagamento_valida = opcoes_de_pagamento.get(opcao_de_pagamento)
        dados_pgto = carrinho["dados_de_pagamentos"]
        dados_pgto["forma_de_pagamento"] = opcao_de_pagamento_valida

        if opcao_de_pagamento_valida:
            if opcao_de_pagamento_valida in ["Cartão de Crédito", "Cartão de Débito", "Pix"]:
                if opcao_de_pagamento_valida == "Pix":
                    pagar_com_pix()
                pagamento_realizado = realizar_pagamento()
                if pagamento_realizado:
                    break
            if opcao_de_pagamento_valida == "Dinheiro":
                pagar_com_dinheiro(carrinho, dados_pgto)
                break
        else:
            print("Opção inválida. Por favor, escolha entre (1- Cartão de Crédito, 2- Cartão de Débito, 3- PIX, 4- Dinheiro).")


# Função "pagar_com_dinheiro", foi criado para receber os valores digitados pelo usuario caso ele opte por pagar em "Dinheiro", fazendo assim tambem os calculos
#   necessarios caso exista algum troco. Utiliza a estrutura de repetição "while True" para receber os valores inseridos pelo usuario e voltando ao inicio da pergunta
#   caso o valor inserido não seja da forma correta dentro do programa. Utiliza de uma estrutura condicional "if" para verificar se os dados foram inseridos corretamente e
#   tambem para verificar e calcular caso exista troco. 
# Recebe os parametros "carrinho, dados_pgto" para acessar os valores necessarios para dar continuidade ao programa.
def pagar_com_dinheiro(carrinho, dados_pgto):
    """
    Processa o pagamento em dinheiro e calcula o troco, se necessário.

    Parâmetros:
        carrinho (dict): O carrinho de compras com os valores finais.
        dados_pgto (dict): O dicionário de dados de pagamento, incluindo o valor do troco.
    """
    while True:
        dinheiro_recebido = input("Valor Recebido: R$ ").strip()
        dinheiro_recebido = validando_dinheiro(dinheiro_recebido)
        
        if dinheiro_recebido is False:
            print("Valor Inválido. Por favor, insira um valor numérico.")

        dinheiro_recebido = dinheiro_recebido * 100
        if dinheiro_recebido >= carrinho["valor_final_com_tributos"]:
            dados_pgto["troco"] = (
                dinheiro_recebido - carrinho["valor_final_com_tributos"]
            )
            print(f"Compra efetuada com sucesso. O troco é de R$ {dados_pgto["troco"]/100:.2f}")
            break
        else:
            print("Valor recebido é insuficiente para efetuar a compra. Por favor, tente novamente.")


# Função "pagar_com_pix", foi criado para utilizar da função "gerar_qr_code" caso o usuario opte em pagar por PIX, gerando assim um Qr Code.
# Utiliza da funcionalidade "sleep" da biblioteca "time" para levar 2 segundos para gerar o Qr Code para o usuario ver.
def pagar_com_pix():
    """
    Gera um QR Code para pagamento via PIX e simula o tempo de processamento com "sleep".
    """
    gerar_qr_code()
    time.sleep(2)


# Função "validando_dinheiro", foi criado para caso o usuario decida pagar em dinheiro, ele utiliza da estrutura de tratamento de erros "Try, except" para
#   validar se o usuario digitou um numero válido, caso não ele retornará False.
# Recebe o parametro "valor" para fazer essa validação e continuar o programa.
def validando_dinheiro(valor):
    """
    Valida se o valor inserido é um número válido.

    Parâmetros:
        valor (str): O valor inserido pelo usuário.

    Retorna:
        float: O valor convertido se for válido.
        bool: False se o valor for inválido.
    """
    try:
        return float(valor)
    except ValueError:
        return False


# Função "relizar_pagamento", fo criado para fazer com que depois da escolha da forma de pagamento, possa haver um erro no pagamento, fazendo assim com que o usuario
#   repita o processo até dar certo, dando continuidade ao programa.
# Utiliza da biblioteca "random" a funcionalidade "getrandbits" onde utiliza do valor booleano da variavel "acerto" gerando valores aleatorios com uma estrutura 
#   condicional "if" para funcionar. 
# Retorna a variavel "acerto" que armazena o valor que foi gerado aleatoriamente.
def realizar_pagamento():
    """
    Simula o pagamento, retornando sucesso ou falha.

    Retorna:
        bool: True para sucesso, False para falha.
    """
    acerto = bool(random.getrandbits(1))
    if acerto:
        print("Pagamento efetivado com sucesso!")
    else:
        print("Falha ao realizar o pagamento. Por favor, tente novamente")

    return acerto


# Função "gerar_qr_code", foi criado para caso o usuario decida pagar com PIX, o programa gera um Qr Code aleatorio para dar continuidade ao programa.
# Utiliza da biblioteca "qrcode" a funcionalidade "QRCode" para gerar a imagem do Qr Code.
def gerar_qr_code():
    """
    Gera um QR Code para pagamento via PIX e exibe no terminal.
    """
    data = "https://www.example.com/"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    img.save("qrcode.png")

    qrcode_terminal.draw(data)
