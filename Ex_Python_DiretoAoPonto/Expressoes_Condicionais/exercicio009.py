# Ex.009 - Crie um simulador de dados. Que gere um valor aleatorio e o imprima em formato de dado:

def simulador_de_dados():
    from random import randint

    print('=============== Simulador de Dados ===============')
    print('Vamos jogar!')
    print('==================================================')

    while True:
        print('\nJogando um dado com valores aleatorios: ')
        valor_aleatorio = randint(1, 6)
        print(f'\nO valor escolhido foi {valor_aleatorio}, dado formatado abaixo: ')

        if valor_aleatorio == 1:
            print('[   ][   ][   ]')
            print('[   ][ ● ][   ]')
            print('[   ][   ][   ]')

        elif valor_aleatorio == 2:
            print('[ ● ][   ][   ]')
            print('[   ][   ][   ]')
            print('[   ][   ][ ● ]')

        elif valor_aleatorio == 3:
            print('[ ● ][   ][   ]')
            print('[   ][ ● ][   ]')
            print('[   ][   ][ ● ]')

        elif valor_aleatorio == 4:
            print('[ ● ][   ][ ● ]')
            print('[   ][   ][   ]')
            print('[ ● ][   ][ ● ]')

        elif valor_aleatorio == 5:
            print('[ ● ][   ][ ● ]')
            print('[   ][ ● ][   ]')
            print('[ ● ][   ][ ● ]')

        elif valor_aleatorio == 6:
            print('[ ● ][   ][ ● ]')
            print('[ ● ][   ][ ● ]')
            print('[ ● ][   ][ ● ]')

        while True:
            opcao_usuario = input('\nDeseja jogar o dado novamente [s/n]: ').strip().lower()
            if opcao_usuario in ['s','n']:
                break
            else:
                print('Opção inválida. Digite "s" para sim e "n" para não.')

        if opcao_usuario == 'n':
            print('Encerrando o programa de simular dados. Obrigado por Jogar!')
            break


simulador_de_dados()