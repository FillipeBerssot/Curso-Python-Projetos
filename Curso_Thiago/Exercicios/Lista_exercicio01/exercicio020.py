# Ex. 020- Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

'''conjunto_n = [1 ,2 ,3 ,4 ,5]
#print(conjunto_n)

maior_conjunto_n = max(conjunto_n)
menor_conjunto_n = min(conjunto_n)

print('Dado o conjunto de numeros [1, 2, 3, 4, 5]')
print(f'O maior numero entre eles será o {maior_conjunto_n}')
print(f'O menor numero entre eles será o {menor_conjunto_n}')

soma = maior_conjunto_n + menor_conjunto_n
print(f'A soma do maior numero mais o menor numero é {soma}.')'''

lista_num = []
num = int(input("digite a quantidade de numeros no conjunto: "))

for i in range(num):
    lista_num.append (int(input("digite um numero inteiro: ")))

max = max(lista_num)
min = min(lista_num)

calculo = max + min

print(f"A soma entre o maior: {max} e o menor: {min} é: {calculo}")