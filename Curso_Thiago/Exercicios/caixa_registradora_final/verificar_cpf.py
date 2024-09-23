def verificar_cpf():
    """
    Verifica se o usuario deseja digitar o cpf ou não.
    Verifica se o que foi digitado pelo usuario está correto ou não.
    Caso nao for digitado cpf, continua o programa sem aparecer o cpf.
    Caso for digitado o cpf, faz a validaçao do cpf,
    verificando se o cpf contem somente numeros e se contem 11 numeros.
    """
    while True:
        inserir_cpf = input("\nDeseja inserir o CPF na nota? (s/n): ").strip().lower()
        if inserir_cpf == 's':
            cpf = input('Digite o seu CPF: ').strip()
            if cpf.isnumeric() and len(cpf) == 11:
                break
            else:
                print("CPF inválido. Por favor, insira 11 dígitos numéricos.")
        elif inserir_cpf == 'n':
            cpf = None
            break
        else:
            print("Opção inválida. Por favor, responda com 's' para sim ou 'n' para não.")
    return cpf