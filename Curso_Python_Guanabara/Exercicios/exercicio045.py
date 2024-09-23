# Desafio 045- Crie um programa que faça o computrador jogar JOKENPÔ com voçê:

import random

print('-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=   JOKENPÔ   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('                               TENTE GANHAR DE MIM                                    ')
print('                      ESCOLHA ENTRE PEDRA, PAPEL E TESOURA                            ')

sua_escolha = str(input('FAÇA SUA ESCOLHA: ')).upper()
lista_pc = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_pc = random.choice(lista_pc)

print(f'VOÇÊ ESCOLHEU {sua_escolha}')
print(f'EU ESCOLHI {escolha_pc}')

if sua_escolha == 'PEDRA' and escolha_pc == "PAPEL":
    print('VOÇE PERDEU, TENTE NOVAMENTE')
elif sua_escolha == "PEDRA" and escolha_pc == "TESOURA":
    print('VOÇÊ GANHOU, PARABENS!')
elif sua_escolha == 'PAPEL' and escolha_pc == "PEDRA":
    print('VOÇÊ GANHOU, PARABENS!')
elif sua_escolha == "PAPEL" and escolha_pc == 'TESOURA':
    print('VOÇÊ PERDEU, TENTE NOVAMENTE')
elif sua_escolha == 'TESOURA' and escolha_pc == 'PAPEL':
    print('VOÇÊ GANHOU, PARABENS!')
elif sua_escolha == 'TESOURA' and escolha_pc == 'PEDRA':
    print('VOÇÊ PERDEU, TENTE NOVAMENTE')
else:
    print('EMPATAMOS, VAMOS TENTAR DE NOVO?')

print('-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
