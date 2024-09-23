import qrcode
import qrcode_terminal

def formas_de_pagamento(total_com_tributo):
    """
    Verifica as formas de pagamento (credito, debito, dinheiro e pix)
    Verifica a forma de pagamento do usuario e utiliza como pagamento
    Caso for dinheiro, verifica se existe troco ou nao e faz o calculo
    Verifica se o troco é valido ou não
    Verifica se a forma de pagamento foi digitada corretamente ou não
    """
    import time
    import random

    while True:
        # Escolha da forma de pagamento
        forma_pagamento = input("\nEscolha a forma de pagamento (1- Cartão de Crédito, 2- Cartão de Débito, 3- PIX, 4- Dinheiro): ").strip()

        if forma_pagamento in ['1', '2', '3', '4']:
            if forma_pagamento == '1':
                forma_pagamento = "Cartão de Crédito"
                dinheiro_recebido = total_com_tributo
                troco = 0
                print('Pagamento Efetuado Com Sucesso.')
                break
            elif forma_pagamento == '2':
                forma_pagamento = "Cartão de Débito"
                dinheiro_recebido = total_com_tributo
                troco = 0
                print('Pagamento Efetuado Com Sucesso.')
                break
            elif forma_pagamento == '3':
                forma_pagamento = "PIX"
                while True:
                    data = "https://www.example.com/"

                    # Gerar QR code e exibir
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=5,
                        border=2,
                    )
                    qr.add_data(data)
                    qr.make(fit=True)

                    img = qr.make_image(fill='black', back_color='white')
                    img.save("qrcode.png")

                    qrcode_terminal.draw(data)
                    time.sleep(2)

                    # Simular sucesso/falha no pagamento PIX
                    if random.choice([True, False]):
                        dinheiro_recebido = total_com_tributo
                        troco = 0
                        print("Pagamento com QR code foi efetuado com sucesso")
                        break
                    else:
                        print("Erro no pagamento, gerando novo QR code...")
                        time.sleep(2)
                break
            elif forma_pagamento == '4':
                forma_pagamento = 'Dinheiro'
                while True:
                    dinheiro_recebido = input('Valor Recebido: R$ ').strip()
                    try:
                        dinheiro_recebido = float(dinheiro_recebido)
                        if dinheiro_recebido >= total_com_tributo:
                            troco = dinheiro_recebido - total_com_tributo
                            print(f'O troco é de R$ {troco:.2f}.')
                            break
                        else:
                            print('Valor insuficiente. Tente novamente.')
                    except ValueError:
                        print('Valor Inválido. Por favor, insira um valor numérico.')
                break
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")

    return forma_pagamento
