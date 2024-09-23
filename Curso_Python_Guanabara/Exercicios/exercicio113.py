# Ex. 113- Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um numero tipo invalido. Aproveite e crie tambem uma função leiaFloat() com a mesma funcionalidade:

def leiaInt():
    while True:
        try:
            numero = int(input('Digite um numero: '))
        except (ValueError, TypeError):
            print('ERRO! Digite um numero inteiro valido.')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return numero

def leiaFloat():
    while True:
        try:
            numero_real = float(input('Digite um numero Real: '))
        except (ValueError, TypeError):
            print(f'Erro! Usuario preferiu não digitar esse numero. ')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return numero_real


numero = leiaInt()
print(f'Voçê acabou de digitar o numero Inteiro {numero}')

numero_real = leiaFloat()
print(f'Voçê acabou de digitar o numero Real {numero_real}')
print(f'O valor inteiro digitado foi {numero} e o real foi {numero_real}')