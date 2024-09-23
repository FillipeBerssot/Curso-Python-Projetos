# Desafio 024- Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO":

nome_cidade = str(input("Digite o nome de uma cidade aleatoria: ")).strip()

print(nome_cidade[:5].upper() == 'SANTO')
