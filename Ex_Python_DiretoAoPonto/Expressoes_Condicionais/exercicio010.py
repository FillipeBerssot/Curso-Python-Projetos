# Ex.010 - Crie um programa que faça a validação de json. O json recebido pelo programa tem que ter os seguintes dados.
# e-mail e telefone:

# Exemplo : {"email": "estevao@gmail.com", "celular": 61981751329}

# Caso falte informação apresente o erro. Caso venha campos diferentes ou adicionais. Apresente erro:

import json
import re

def validar_json_email_telefone(json_string):
 
    try:
        dados = json.loads(json_string)
    except json.JSONDecodeError:
        return 'Erro: O formato do JSON é inválido.'

    chaves_esperadas = {"email", "celular"}

    if set(dados.keys()) != chaves_esperadas:
        return 'Erro: O JSON deve conter apenas "email" e "celular".'

    padrao_email = r'^[\w\.-]+@[a-z\d-]+\.[a-z]{2,}$'
    if not re.match(padrao_email, dados.get("email", "")):
        return 'Erro: O formato do e-mail é inválido.'

    padrao_celular = r'^\(?\d{2}\)? ?9\d{4} ?\d{4}$'
    if not re.match(padrao_celular, dados.get("celular", "")):
        return 'Erro: O formato do número de celular é inválido.'

    return 'JSON é válido.'


json_exemplo = '{"email": "estevao@gmail.com", "celular": "61981751329"}'
resultado = validar_json_email_telefone(json_exemplo)
print(resultado)

json_invalido = '{"email": "email_invalido", "celular": "61981751329"}'
resultado = validar_json_email_telefone(json_invalido)
print(resultado)

json_com_erro = '{"email": "estevao@gmail.com", "celular": "61981751329", "nome": "Estevao"}'
resultado = validar_json_email_telefone(json_com_erro)
print(resultado)
