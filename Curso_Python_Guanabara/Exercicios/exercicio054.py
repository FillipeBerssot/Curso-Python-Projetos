# Ex.054- Crie um pograma que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores:

from datetime import date
ano_atual = date.today().year

total_maior = 0
total_menor = 0
for pessoas in range(1, 8):
    nascimento = int(input(f'Em que ano a pessoa {pessoas} pessoa nasceu? '))
    idade = ano_atual - nascimento
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f'\nAo todo tivemos {total_maior} pessoas maiores de idade.')
print(f'E tambem tivemos {total_menor} pessoas menores de idade.')