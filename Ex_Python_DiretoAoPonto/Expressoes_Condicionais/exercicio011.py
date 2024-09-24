# Ex.011 - Faça um validador de CPF:

# CPF tem o formato XXX.XXX.XXX-YY
# 9 digitos principais: XXX.XXX.XXX
# 2 digitos verificadores: YY

import re


print('=============== Verificador de CPF ===============')
print('Verifique se o seu CPF é Válido ou Não!')
print('==================================================')

def validar_cpf(cpf):

    erros = []

    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        erros.append('\nCPF Inválido. O CPF deve estar no formato XXX.XXX.XXX-YY.')
    
    cpf_sem_formatacao = re.sub('[^0-9]', '', cpf)

    if len(cpf_sem_formatacao) != 11:
        erros.append('\nCPF Inválido. CPF digitado não contem 11 digitos.')
    else:
        if cpf_sem_formatacao == cpf_sem_formatacao[0] * 11:
            erros.append('\nCPF Inválido. Todos os digítos são iguais.')
        
        soma = 0
        for i in range(9):
            soma += int(cpf_sem_formatacao[i]) * (10 - i)

        resto = (soma * 10) % 11
        if resto == 10 or resto == 11:
            resto = 0

        if resto != int(cpf_sem_formatacao[9]):
            erros.append('\nCPF Inválido. Primeiro dígito verificador está incorreto.')
        
        soma = 0
        for i in range(10):
            soma += int(cpf_sem_formatacao[i]) * (11 - i)

        resto = (soma * 10) % 11
        if resto == 10 or resto == 11:
            resto = 0

        if resto != int(cpf_sem_formatacao[10]):
            erros.append('\nCPF Inválido. Segundo dígito verificador está incorreto.')
    
    if not erros:
        return '\nCPF Válido.'
    else:
        return '\n'.join(erros)


cpf = input('\nDigite aqui o CPF que voçê quer validar no formato XXX.XXX.XXX-YY: ').strip()
print(validar_cpf(cpf))