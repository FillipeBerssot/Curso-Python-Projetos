# Ex.076- Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular:

produtos = ('Pão', 1.50, 'Leite', 3.25, 'Frango', 19.90, 'Carne', 34.90, 'Café', 14.90, 'Ovos', 13.90, 'Alface', 3.99, 'Tomate', 4.99)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='')
    else:
        print(f'R${produtos[posicao]:>8.2f}')
print('-' * 40)
