# Ex.005 - Escreva um programa para imprimir números maiores que a média:

def numeros_maiores_media(lista_numeros):
    media = sum(lista_numeros) / len(lista_numeros)
    maiores_media = []
    for i in lista_numeros:
        if i > media:
            maiores_media.append(i)

    return f'Os números dentro da lista: {lista_numeros} que são maiores do que a média dessa lista: {media:.2f}, são os números: {maiores_media}'


lista_numeros = [12, 5, 55, 10, 12, 44]
print(numeros_maiores_media(lista_numeros))

lista_numeros2 = [1, 2, 3, 4, 5]
print(numeros_maiores_media(lista_numeros2))
