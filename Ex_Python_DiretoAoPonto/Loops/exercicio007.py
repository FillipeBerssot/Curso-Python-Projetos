# Ex.007 - Escreva um algoritmo de busca linear:

def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return f'O valor {valor} foi encontrado na {i + 1}º posição.'
        
    return f'O valor {valor} não foi encontrado na lista.'
        

lista = [1, 2, 4, 5, 7, 10]
print(busca_linear(lista, 11))

lista2 = [1, 2, 4, 5, 7, 10]
print(busca_linear(lista2, 7))
