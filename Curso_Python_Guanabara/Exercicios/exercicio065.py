# Ex.065- Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, 
# mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuario se ele quer ou não continuar a digitar valores:

numeros = 0
opcao = 'S'
soma = 0
quantidade = 0
media = 0
maior = 0
menor = 0

while opcao in 'Ss':
    numeros = int(input('Digite aqui varios numeros: '))
    soma += numeros
    quantidade += 1
    if quantidade == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros


    opcao = input('Quer continuar? [S / N]: ').strip().upper()[0]
media = soma / quantidade
print(f'Voçê digitou {quantidade} numeros e a media deles foi {media}.')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}.')
