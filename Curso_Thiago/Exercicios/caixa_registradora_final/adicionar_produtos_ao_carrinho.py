from produtos import lista_de_mercadorias

def adicionar_produtos_ao_carrinho(carrinho, quantidades):
    """
    Verifica se o codigo de barras existe e se esta sendo digitado
    corretamente.
    Se nao existe ou digitou errado, avisa o usuario.
    Se existe adiciona a lista.
    Verifica se o codigo de barras ja existe dentro de uma lista e
    se existir adiciona o produto novamente 
    
    """
    while True:
        codigo_de_barras = input("Código de barras: ").strip()

        # Se o código de barras for '0' e o carrinho estiver vazio, impedir continuação
        if codigo_de_barras == '0' and not carrinho:
            print("Não é possível prosseguir sem nada.")
        # Se o código de barras for '0' e houver itens no carrinho, sair do loop
        elif codigo_de_barras == '0':
            break
        
        elif not codigo_de_barras.isnumeric():  # Verificar se o código de barras é numérico
            print("Código de barras inválido. Tente novamente.")
        else:
            # Verificar se o código de barras existe na lista de mercadorias
            for mercadoria in lista_de_mercadorias:
                if mercadoria["codigo_de_barras"] == codigo_de_barras:
                    if codigo_de_barras in quantidades:
                        quantidades[codigo_de_barras] += 1
                    else:
                        carrinho.append(mercadoria)
                        quantidades[codigo_de_barras] = 1
                    print(f"Produto adicionado: {mercadoria['nome']} - R$ {mercadoria['preco'] / 100:.2f}")
                    break
            else:
                print("Código de barras não encontrado. Tente novamente.")
                
    return carrinho, quantidades
