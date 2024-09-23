import re       # ---> O pograma está importando a biblioteca "re", "Expressões Regulares", para utilizar de seus recursos durante o programa.
                #           Está fazendo uma importação completa da biblioteca.


# Função "inserir_cpf", foi criado para o usuario digitar o cpf durante o programa, utiliza de estruturas condicionais "if, elif, else" para fazer a validação
#   dos dados inseridos, caso o usuario opte por não digitar o cpf o programa salva e da continuidade sem o cpf inserido.
def inserir_cpf():
    """
    Permite que o usuário insira o CPF e valida sua formatação.
    Se o usuário optar por inserir o CPF, a função valida se o número possui 11 dígitos.
    Se o usuário optar por não inserir, o valor "Não informado" é retornado.
    Retorna:
        str: O CPF validado ou "Não informado".
    """
    while True:
        resposta = input("\nDeseja inserir o CPF na nota? (s/n): ").strip().lower()

        if resposta == "s":
            cpf = input("Digite o seu CPF(11 digitos, sem ponto e traço): ").strip()
            if validar_cpf(cpf):
                print(f"CPF inserido é válido: {cpf}")
                return cpf
            else:
                print("CPF inserido é inválido. Por favor, somente os 11 número sem traço e ponto.")
        elif resposta == "n":
            cpf = "Não Informado"
            return cpf
        else:
            print(
                "Opção inválida. Por favor, responda com 's' para sim ou 'n' para não."
            )


# Função "validar_cpf", foi criado para validar o cpf inserido pelo usuario, retornando um valor booleano onde utiliza da biblioteca "re" para
#   validar se os numeros digitados pelo usuario tem realmente 11 digitos. 
# Utiliza o parametro "cpf" para realizar essa validação.
def validar_cpf(cpf):
    """
    Valida se o CPF fornecido contém exatamente 11 dígitos numéricos.
    Parâmetros:
        cpf (str): O CPF fornecido pelo usuário.
    Retorna:
        bool: True se o CPF for válido (contém 11 dígitos), False caso contrário.
    """
    return bool(re.fullmatch(r"\d{11}", cpf))
