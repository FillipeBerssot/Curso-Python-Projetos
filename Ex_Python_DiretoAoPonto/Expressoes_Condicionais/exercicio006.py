# Ex.006 - Escreva um verificador de validade de senha. O programa deve receber uma senha e verificar se ela atende aos seguintes criterios:

# Pelo menos uma letra maiuscula:
# Pelo menos uma letra minuscula:
# Pelo menos um número:
# Pelo menos um simbolo especial:

def validar_senha(senha):
    if len(senha) < 8:
        return 'Sua senha é inválida. Senha deve conter pelo menos 8 caracteres.'

    tem_maiuscula = any(char.isupper() for char in senha)
    tem_minuscula = any(char.islower() for char in senha)
    tem_numero = any(char.isdigit() for char in senha)
    tem_simbolo = any(not char.isalnum() for char in senha)

    if tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo:
        return 'Sua senha é válida!'
    else:
        mensagem_de_erro = 'Sua senha é inválida. Verifique os critérios:'

        if not tem_maiuscula:
           mensagem_de_erro += '\n- Faltou pelo menos uma Letra Maiúscula na sua senha.'
        if not tem_minuscula:
            mensagem_de_erro += '\n- Faltou pelo menos uma Letra Minúscula na sua senha.'
        if not tem_numero:
            mensagem_de_erro += '\n- Faltou pelo menos um Número na sua senha.'
        if not tem_simbolo:
            mensagem_de_erro += '\n- Faltou pelo menos um Símbolo na sua senha.'
        
        return mensagem_de_erro


senha = input('Digite aqui uma Senha: ')
print(validar_senha(senha))