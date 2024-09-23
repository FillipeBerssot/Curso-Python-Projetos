# Ex.099- Faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior:

from time import sleep

# Maneira 01:
def maior1(* num):
    contador = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if contador == 0:
            maior == valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior1(2, 9, 4, 5, 7, 1)
maior1(4, 7, 0)
maior1(1, 2,)
maior1(6)
maior1(0)

# Maneira 02:
def maior(* numeros):
    print('-=' * 40)
    print('Analisando os valores informados...')
    sleep(1)

    if len(numeros) == 1 and numeros[0] == 0:
        print(f'Os números informados foram: 0. Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:   
        maior_valor = max(numeros)
        numeros_formatados = ', '.join(str(num) for num in numeros)
        print(f'Os numeros informados foram: {numeros_formatados}. Foram informados {len(numeros)} valores ao todo.')
        print(f'O maior valor informado foi {maior_valor}.')
    print('-=' * 40)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2,)
maior(6)
maior(0)
