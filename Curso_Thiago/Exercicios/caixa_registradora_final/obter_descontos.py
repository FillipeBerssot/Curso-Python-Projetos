def obter_desconto(quantidade):
    """
    Serve para obter os descontos nos produtos
    1º desconto = 20% (acima de 10 unidades)
    2º desconto = 15% (acima de 5 unidades)
    3º desconto = 10% (acima de 3 unidades)
    """
    descontos_10_unidades = 0.20
    descontos_5_unidades = 0.15
    descontos_3_unidades = 0.10

    if quantidade >= 10:
        return descontos_10_unidades
    elif quantidade >= 5:
        return descontos_5_unidades
    elif quantidade >= 3:
        return descontos_3_unidades
    else:
        return 0.00