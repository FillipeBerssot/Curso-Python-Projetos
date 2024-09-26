# Ex.002 - Escreva um programa que calcule a média da lista = [1, 2, 3, 4, 5]:

def calcular_media(lista):
    if lista:
        media_lista = sum(lista) / len(lista)
        return f'A média da lista inserida ({lista}) é: {media_lista}'
    else:
        return 0 

lista = [1, 2, 3, 4, 5]
print(calcular_media(lista))

lista2 = [1,10,15,2,5,30]
print(calcular_media(lista2))

lista3 = []
print(calcular_media(lista3))
