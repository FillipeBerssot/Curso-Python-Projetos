# Ex.07- Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

lista_numero = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
]

print('Escolha de qual forma voçê quer acessar a lista de numeros:')
print('Digite [ 1 ] para acessar a lista um numero abaixo do outro')
print('Digite [ 2 ] para acessar a lista um numero ao lado do outro')
escolha = int(input(' '))

if escolha == 1:
    print(lista_numero[0])
    print(lista_numero[1])
    print(lista_numero[2])
    print(lista_numero[3])
    print(lista_numero[4])
    print(lista_numero[5])
    print(lista_numero[6])
    print(lista_numero[7])
    print(lista_numero[8])
    print(lista_numero[9])
    print(lista_numero[10])
    print(lista_numero[11])
    print(lista_numero[12])
    print(lista_numero[13])
    print(lista_numero[14])
    print(lista_numero[15])
    print(lista_numero[16])
    print(lista_numero[17])
    print(lista_numero[18])
    print(lista_numero[19])
elif escolha == 2:
    print(lista_numero)
