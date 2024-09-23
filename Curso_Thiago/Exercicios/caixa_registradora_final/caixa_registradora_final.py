from produtos import lista_de_mercadorias
from obter_data_hora_atual import obter_data_hora_atual
from obter_taxa_tributo import obter_taxa_tributo
from obter_descontos import obter_desconto
from adicionar_produtos_ao_carrinho import adicionar_produtos_ao_carrinho
from formas_de_pagamento import formas_de_pagamento
from verificar_cpf import verificar_cpf
from resumo_da_compra import resumo_da_compra
from impressao_da_nota_fiscal import impressao_da_nota_fiscal
from registrar_nova_compra import registrar_nova_compra

# Constantes para tributos e descontos:
# Usei a função obter_taxa_tributo e obter_data_hora_atual
taxa_do_tributo = obter_taxa_tributo()
data_hora_atualizado = obter_data_hora_atual()

# Loop principal para registrar uma nova compra:
while True:
    carrinho, quantidades = [], {}

    print("Digite os códigos de barras dos produtos (digite '0' para finalizar):")

    # Verificar o codigo de barras:
    # Usei a função verificacao_do_codigo_de_barras
    carrinho, quantidades = adicionar_produtos_ao_carrinho(carrinho, quantidades)

    # Inicializar os totais:
    # Usei a função resumo_da_compra
    total_com_tributo, total, total_com_desconto = resumo_da_compra(carrinho, quantidades, obter_desconto, taxa_do_tributo)

    # Mostrar totais:
    print(f"Total da compra (sem os descontos e tributos): R$ {total / 100:.2f}")
    print(f"Total da compra com os descontos: R$ {total_com_desconto / 100:.2f}")
    print(f"Total da compra com o desconto e os tributos (15.17%): R$ {total_com_tributo / 100:.2f}")

    total_com_tributo = total_com_tributo / 100
    
    # Escolha da forma de pagamento:
    # Usei a função formas_de_pagamento
    forma_pagamento = formas_de_pagamento(total_com_tributo)

    # Inserir CPF na nota:
    # Usei a função inserir_cpf
    cpf = verificar_cpf()

    # Dicionario com os dados da compra:
    dados_compra = {
        'data_hora': data_hora_atualizado,
        'cpf' : cpf,
        'forma_pagamento' : forma_pagamento,
        'carrinho' : carrinho,
        'quantidades' : quantidades,
        'total' : total,
        'total_com_desconto' : total_com_desconto,
        'total_com_tributo' : total_com_tributo,
        'obter_descontos' : obter_desconto
    }

    # Impressão da Nota Fiscal:
    # Usei a função impressao_da_nota_fiscal
    impressao_da_nota_fiscal(dados_compra)

    # Registrar uma nova compra:
    # Usei a função registrar_nova_compra
    nova_compra_usuario = registrar_nova_compra()
    if nova_compra_usuario == 'n':
        print('Encerrando o Sistema. Obrigado e Volte Sempre!')
        break