def obter_velocidade_do_usuario():
    """
    Objetivo: Obter a resposta de velocidade do usuario, faz
    uma validação da resposta e faz o retorno dessa resposta
    em um valor númerico.

    Exibe uma lista de opções.

    Realiza a validação dessa opção.
    """

    opcoes_velocidade = """
Escolha a velocidade de reprodução:
[1] - 0.25x
[2] - 0.5x
[3] - 0.75x
[4] - 1.25x
[5] - 1.5x
[6] - 1.75x
[7] - 2.0x
"""
    print(opcoes_velocidade)

    velocidades = {
        '1': 0.25,
        '2': 0.5,
        '3': 0.75,
        '4': 1.25,
        '5': 1.5,
        '6': 1.75,
        '7': 2.0,
    }

    opcao_velocidade = input('Digite sua escolha: ').strip()
    while opcao_velocidade not in velocidades:
        print('Opção inválida. Escolha uma opção válida entre 1 e 7.')
        opcao_velocidade = input('Digite sua escolha: ').strip()

    return velocidades[opcao_velocidade]
