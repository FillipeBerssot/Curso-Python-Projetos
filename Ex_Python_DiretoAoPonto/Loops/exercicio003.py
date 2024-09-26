# Ex.003 - Escreva um programa que ache o maior valor de uma lista = [1, 2, 3, 4, 5]:

def achar_maior_valor(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
            
    return f'Na lista inserida ({lista}) o maior valor é: {maior}'


lista = [1, 2, 3, 4, 5]
print(achar_maior_valor(lista))
