# Ex.059- Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar = feito
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso:

from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('----------------------- MENU -----------------------')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior valor')
    print('[ 4 ] Adicionar novos numeros')
    print('[ 5 ] Sair do programa')

    opcao = int(input('Qual é a sua opcão: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre o primeiro valor {n1} e o segundo valor {n2} é: {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'A multiplicação entre o primeiro valor {n1} e o segundo valor {n2} é: {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre o primeiro valor {n1} e o segundo valor {n2} é: {maior}')
    elif opcao == 4:
        print('Informe os novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando o programa...')
    else:
        print('Opção invalida. Tente novamente')
    sleep(2)
print('Fim do programa! Obrigado e volte sempre!')

