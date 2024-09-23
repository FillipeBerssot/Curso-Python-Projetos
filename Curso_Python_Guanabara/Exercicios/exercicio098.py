# Ex.098- Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo e realize contagem.
# Seu programa tem que realizar três contagens atraves da função criada:
# A) De 1 até 10, de 1 em 1:
# B) De 10 até 0, de 2 em 2:
# C) Uma contagem personalizada:

from time import sleep

def linha():
    print('=' * 40)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
        
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    sleep(1)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='',flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')


# A) 1 ate 10, 1  em 1:
linha()
contador(1,10,1)
# B) 10 ate 0, 2 em 2:
linha()
contador(10, 0, 2)
# C) Personalizado:
linha()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Digite o Inicio: '))
fim = int(input('Digite o Fim: '))
passo = int(input('Digite o Passo: '))
linha()
contador(inicio, fim, passo)