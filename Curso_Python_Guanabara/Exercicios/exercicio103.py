# Ex. 103- Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: 
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente:

def ficha(nome, gols):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if not str(gols).isdigit():
        gols = 0
        
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = input('Nome do Jogador: ').strip().capitalize()
gols = input('Número de Gols: ').strip()
print(ficha(nome,gols))