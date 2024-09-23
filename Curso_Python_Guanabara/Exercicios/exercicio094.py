# Ex.094 - Crie um programa que leia o nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas: FEITO
# B) A média de idade do grupo: FEITO
# C) Uma lista com todas as mulheres: FEITO
# D) Uma lista com todas as pessoas com idade acima da média:

# Maneira 01:
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = input('Nome: ')
    while True:
        pessoa['Sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']

    galera.append(pessoa.copy())
    while True:
        resposta = input('Quer continuar? [S/N]: ').upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

print('-=' * 40)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradasa foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p['Nome']} ', end='')
print()
print('D) Lista das pessoas que estão acima da media: ', end='')
for p in galera:
    if p['Idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

# Maneira 02:
dados_pessoas_lista = []

while True:
    pessoas = {}
    pessoas['Nome'] = input('Nome: ').strip().capitalize()
    pessoas['Sexo'] = input('Sexo, digite [M] para masculino e [F] para feminino: ').strip().upper()
    pessoas['Idade'] = int(input('Digite a idade: '))

    dados_pessoas_lista.append(pessoas)

    opcao = input('Deseja continuar?[S/N]: ').strip().upper()
    if opcao == 'N':
        print('Programa Encerrado.')
        break
print('-=' * 50)
print(dados_pessoas_lista)
# A):
print('-=' * 50)
print(f'Foram cadastradas no grupo {len(dados_pessoas_lista)} pessoas.')
# B):
soma_das_idade = 0
for pessoa in dados_pessoas_lista:
    soma_das_idade += pessoa['Idade']
if len(dados_pessoas_lista) > 0:
    media_idade = soma_das_idade / len(dados_pessoas_lista)
else:
    media_idade = 0
print(f' - A média de idade do grupo é: {media_idade:.2f}')
# C): 
mulheres = []
for pessoa in dados_pessoas_lista:
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
print(f' - As mulheres na lista são: {mulheres}')
# D) :
acima_da_media = []
for pessoa in dados_pessoas_lista:
    if pessoa['Idade'] > media_idade:
        acima_da_media.append(pessoa['Nome'])
print(f' - As pessoas do grupo com idade acima da media({media_idade:.2f}) = {acima_da_media}')
print('-=' * 50)