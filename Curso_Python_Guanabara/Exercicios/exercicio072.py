# Ex.072- Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extensao, de zero até vinte.
# Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso:

contagem = (
    'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
    'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 
    'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Voçe digitou o numero {contagem[numero]}.')  
    else:
        print('Opção invalida. Digite um numero entre 0 e 20') 

    opcao = input('Deseja continuar?[s/n]: ').lower().strip()
    if opcao == 'n':
        print('Encerrando o Programa.')
        break



