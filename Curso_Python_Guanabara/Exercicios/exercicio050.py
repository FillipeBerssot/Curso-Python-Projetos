# Ex.050- Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for impar, desconsidere-o:

soma = 0
contador = 0
for x in range(1, 7):
    numero = int(input(f'Digite aqui o {x}º numero: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f'A soma dos {contador} numeros pares é igual a {soma}')
