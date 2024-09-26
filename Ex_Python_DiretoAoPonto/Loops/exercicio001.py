# Ex.001 - Escreva um programa que some os itens da lista = [1, 2, 3, 4, 5]:

def somar_itens_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return f'A soma de todos os itens da lista inserida ({lista}) é: {soma}'


lista = [1, 2, 3, 4, 5]
print(somar_itens_lista(lista))
