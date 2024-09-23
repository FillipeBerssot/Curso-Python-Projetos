# Ex.064- Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999,
# que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles:
# (desconsiderando o flag)

contador = 0
soma = 0
numero = 0

while numero != 999:
    numero = int(input('Digite aqui varios numeros (Digite 999 para parar): '))
    if numero != 999:
        contador += 1
        soma += numero
print(f'Acabou. Voçê digitou {contador} numeros e a soma entre eles foi {soma}.')
