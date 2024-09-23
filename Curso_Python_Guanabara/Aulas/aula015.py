# Continuação da estrutura de repetição com teste logico, WHILE:
# WHILE == enquanto
# Break == interrompa

# Exemplo:
'''cont = 1
while cont <= 10:
    print(cont, ' -> ', end='')
    cont += 1
print('FIM')'''

#Exemplo:
'''n = 0
cont = 0
while cont < 5:
    n = int(input('Digite um numero: '))
    cont += 1'''

# Exemplo:
'''numero = 0
while numero != 999:
    numero = int(input('Digite um numero: '))'''

# Exemplo com o comando BREAK:
n = 0 
s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')