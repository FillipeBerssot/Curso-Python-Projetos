# Ex.055- Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos:


maior_peso = 0
menor_peso = 0

for p in range(1,6):
    peso = float(input(f'Digite o peso da {p} pessoas em kgs: '))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'\nNa lista criada com o peso de 5 pessoas o maior peso lido foi: {maior_peso} kgs.')
print(f'Na lista criada com o peso de 5 pessoas o menor peso lido foi: {menor_peso} kgs.')
    