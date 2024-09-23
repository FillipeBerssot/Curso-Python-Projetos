# CONDIÇÕES ANINHADAS:
# Exemplo 01:

""" if carro.esquerda():
    bloco1
elif carro.direita():
    bloco2
elif carro.ré():
    bloco3
else:
    bloco4 """

# Exemplo 02:

nome = str(input('Qual é o seu nome? '))
if nome == 'Fillipe':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular aqui no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um Bom Dia {nome}, até mais!')

