# Ex.089- Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente:

notas_gerais = []

while True:
    nome = input('Digite o nome do aluno: ').strip().capitalize()
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))

    media = (nota1 + nota2) / 2
    aluno = [nome, nota1, nota2, media]
    notas_gerais.append(aluno)
    
    opcao = input('Quer continuar?[S / N]: ').strip().upper()
    if opcao == 'N':
        break

print('\nBoletim:')
print(f'{'Indice':6} {'Nome':<10} {'Média':>8}')
print('-' * 30)

for i, v in enumerate(notas_gerais):
    nome = v[0]
    media = v[3]
    print(f'{i:<6} {nome:<10} {media:>8.2f}')
print('-' * 30)

while True:
    opcao02 = input('\nVoçê quer ver as notas de qual aluno?[Digite o indice ou [S] para sair]: ').strip()

    if opcao02.lower() == 's':
        break

    if opcao02.isdigit():
        indice = int(opcao)
        if 0 <= indice < len(notas_gerais):
            aluno = notas_gerais[indice]
            print(f'\nNotas de {aluno[0]}: ')
            print(f'Primeira Nota: {aluno[1]}: ')
            print(f'Segunda Nota: {aluno[2]}')
            print(f'Média: {aluno[3]:.2f}')
        else:
            print('Indice Invalido. Tente Novamente.')
    else:
        print('Opção Invalida. Tente Novamente.')