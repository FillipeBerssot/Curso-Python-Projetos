# Estrutura de repetição com teste logico, WHILE:
# WHILE == enquanto

# Exemplo 01:
c = 1 
while c != 11:
    print(c)
    c += 1
print('acabou')

# Exemplo 02:
repetir = 'S'
while repetir == 'S':
    numero = int(input('Digite um valor: '))
    repetir = str(input('Quer continuar? [S / N] ')).upper()
print('FIM')

# Exemplo 03:
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voçê digitou {par} numero pares e {impar} impares!')