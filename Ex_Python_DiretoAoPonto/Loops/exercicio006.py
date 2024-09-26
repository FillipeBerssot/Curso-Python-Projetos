# Ex.006 - Escreva um programa que conte o numero de ocorrencias do numero 2 na lista = [1, 2, 3, 4, 2, 2, 5, 2, 6]:

def contar_ocorrencias(lista, elemento):
    contagem = 0
    for item in lista:
        if item == elemento:
            contagem += 1
    return f'Na lista inserida {lista} o numero {elemento} ocorreu {contagem} vezes.'


lista = [1, 2, 3, 4, 2, 2, 5, 2, 6]
print(contar_ocorrencias(lista, 2))
