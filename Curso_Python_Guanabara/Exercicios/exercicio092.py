# Ex.092- Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario se por acaso o
# CTPS for diferente de ZERO, o dicionario recebera tambem o ano de contratação e o salario. Calcule e acrescente
# além, da idade, com quantos anos a pessoa vai se aposentar:
# Se aposenta depois de 35 anos de contribuição.

while True:
    nome = input('Nome: ').capitalize()
    ano_nascimento = int(input('Ano de Nascimento: '))
    idade = 2024 - ano_nascimento

    ctps = int(input('Carteira de Trabalho (0 não tem): '))
    dados_clt = {'Nome': nome, 'Idade': idade, 'CTPS': ctps}

    if ctps != 0:
        ano_contratacao = int(input('Ano de Contratação: '))
        salario = float(input('Salario: '))
        dados_clt['Ano de Contratação'] = ano_contratacao
        dados_clt['Salario'] = salario
        anos_contribuicao = 2024 - ano_contratacao
        idade_aposentadoria = idade + (35 - anos_contribuicao)
        dados_clt['Idade de Aposentadoria'] = idade_aposentadoria
    elif ctps == 0:
        print('CTPS igual a ZERO. Não há dados suficientes.')
    opcao = input('Quer Continuar?[S/N]: ').strip().upper()
    if opcao == 'N':
        break

print('-=' * 30)
print('DADOS DO CONTRIBUINTE: ')
print(f'\n  - Nome: {nome}')
print(f'  - Idade: {idade}')
print(f'  - CTPS: {ctps}')
print(f'  - Ano de Contratação: {ano_contratacao}')
print(f'  - Salario: {salario}')
print(f'  - Idade para se aposentar: {idade_aposentadoria}')
print('-=' * 30)