def inserir_cpf():
    while True:
        inserir_cpf = (
            input('\nDeseja inserir o CPF na nota? (s/n): ').strip().lower()
        )
        if inserir_cpf == 's':
            cpf = input('Digite o seu CPF: ').strip()
            if cpf.isnumeric() and len(cpf) == 11:
                print('cpf')
                break
            else:
                print('CPF inválido. Por favor, insira 11 dígitos numéricos.')
        elif inserir_cpf == 'n':
            cpf = None
            break
        else:
            print(
                "Opção inválida. Por favor, responda com 's' para sim ou 'n' para não."
            )
