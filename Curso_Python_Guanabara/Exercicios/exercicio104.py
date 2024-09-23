# Ex. 104- Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numerico:
# Ex:
#   n = leiaInt('Digite um numero: ')

def leiaInt(numero):
    while True:
        numero = input('Digite um numero: ')
        if numero.isdigit():
            return int(numero)
        else:
            print('Erro! Digite um numero inteiro válido.')



numero = leiaInt('Digite um numero: ')
print(f'Voçê acabou de digitar o numero {numero}')