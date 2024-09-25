# Ex.012 - Faça um programa que armazene os aniversarios de amigos. Verifique se o dia de hoje é
# o aniversario de um deles:

import time

def armazenar_aniversarios():
    data_atual = time.strftime("%d/%m/%Y", time.localtime())
    data_formatada = data_atual
    aniversarios_amigos = []

    while True:
        amigos = {}

        amigos['Nome'] = input('Digite o Nome do seu Amigo(a): ').strip().capitalize()
        amigos['Data de Aniversario'] = input('Digite a data de aniversario do seu Amigo(a): ')
        aniversarios_amigos.append(amigos)

        opcao = input('\nDeseja Adicionar mais algum amigo(a), digite "s" para sim e "n" para não: ').strip()[0]

        if opcao == 'n':
            print('\nEncerrando o Programa. Abaixo está os dados inseridos: ')
            break

    for amigos in aniversarios_amigos:
        print(f'Nome: {amigos["Nome"]}; Data de Aniversario: {amigos['Data de Aniversario']}')

    for amigo in aniversarios_amigos:
        if amigo['Data de Aniversario'] == data_formatada:
            print(f'\nHoje, dia {data_formatada} é o aniversario de {amigos["Nome"]}, lembre-se de dar os parabéns!')
        else:
            print('\nNinguem faz aniversario hoje.')
            break

armazenar_aniversarios()
