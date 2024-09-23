# Ex.097- Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro
# e mostre uma mensagem com tamanho adptavel:
# Ex:
#   escreva('Olá, Mundo!)
# Saída:
#   ~~~~~~~~~~~~
#   Olá, Mundo! 
#   ~~~~~~~~~~~~

def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)


escreva('Gustavo Guanabara')
escreva('CURSO DE PYTHON NO YOUTUBE')
escreva('CeV')
txt = input('Digite um texto qualquer: ')
escreva(txt)