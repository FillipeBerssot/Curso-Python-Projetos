# Desafio 041- A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 ano: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SENIOR
# - Acima de 25: MASTER


print('=============   Seja Bem Vindo a Confederação Nacional de Natação    =============')
print('========= Faça Sua Inscrição é Descubra Em Qual Categoria Voçê Se Enquadra =======')

nome = str(input('Digite aqui o seu nome completo: '))
ano_nascimento = float(input('Digite aqui o ano de nascimento: '))
ano_atual = float(input('Digite em que ano nós estamos atualmente: '))

idade_participante = ano_atual - ano_nascimento

print(f'Olá {nome}, de acordo com o que foi informado voçê tem {idade_participante:.0f} anos.')
print('Sua Categoria será: ')

if idade_participante <= 9:
    print('==========  MIRIM  ==========')
elif idade_participante <= 14:
    print('==========  INFANTIL ========')
elif idade_participante <= 19:
    print('==========  JUNIOR  ==========')
elif idade_participante <= 25:
    print('==========  SENIOR  ==========')
else:
    print('==========  MASTER  ==========')
print('==========================   OBRIGADO PELA INSCRIÇÃO   ===========================')