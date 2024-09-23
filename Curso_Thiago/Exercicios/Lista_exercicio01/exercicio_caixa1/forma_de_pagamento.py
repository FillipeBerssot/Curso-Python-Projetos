import random
import time
import qrcode
import qrcode_terminal


def forma_de_pagamento(compra):
    lista_de_opcoes_de_pagamento = ["1", "2", "3", "4"]
    dados_de_pagamento = {
        "dinheiro_recebido": compra["total_com_tributo"],
        "troco": 0,
        "tipo": None,
    }

    while True:
        forma_pagamento = input(
            "\nEscolha a forma de pagamento (1- Cartão de Crédito, 2- Cartão de Débito, 3- PIX, 4- Dinheiro): "
        ).strip()

        if forma_pagamento in lista_de_opcoes_de_pagamento:
            if forma_pagamento == lista_de_opcoes_de_pagamento[0]:
                dados_de_pagamento["tipo"] = "Cartão de Crédito"
                pagamento_realizado = realizar_pagamento()
                if pagamento_realizado:
                    break
            elif forma_pagamento == lista_de_opcoes_de_pagamento[1]:
                dados_de_pagamento["tipo"] = "Cartão de Débito"
                pagamento_realizado = realizar_pagamento()
                if pagamento_realizado:
                    break
            elif forma_pagamento == lista_de_opcoes_de_pagamento[2]:
                while True:
                    dados_de_pagamento["tipo"] = "PIX"
                    gerar_qr_code()
                    time.sleep(2)
                    pagamento_realizado = realizar_pagamento()

                    if pagamento_realizado:
                        break

                    print("erro no pagamento, gerando novo QR code: ")
                    gerar_qr_code()
                    time.sleep(2)

                break

            elif forma_pagamento == lista_de_opcoes_de_pagamento[3]:
                dados_de_pagamento["tipo"] = "Dinheiro"
                while True:
                    dinheiro_recebido = input("Valor Recebido: R$ ").strip()
                    if dinheiro_recebido.replace(".", "", 1).isdigit():
                        dinheiro_recebido = float(dinheiro_recebido)
                        if dinheiro_recebido >= compra["total_com_tributo"]:
                            troco = dinheiro_recebido - compra["total_com_tributo"]
                            dados_de_pagamento["troco"] = troco
                            print(f"O troco é de R$ {troco:.2f}.")
                            break
                        else:
                            print("Valor insuficiente. Tente novamente.")
                    else:
                        print("Valor Invalido. Por favor, insira um valor numerico.")
                break
            else:
                print(
                    "Houve um problema com a forma de pagamento escolhida. Por favor tente novamente."
                )
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")


def gerar_qr_code():
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


def realizar_pagamento():
    acerto = bool(random.getrandbits(1))
    if acerto:
        print("Pagamento Efetivado com sucesso")
    else:
        print("Falha no pagamento, tente novamente")

    return acerto