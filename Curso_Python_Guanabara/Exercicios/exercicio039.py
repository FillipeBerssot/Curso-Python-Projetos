# Desafio 039- Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar:
# - Se é a hora de se alistar:
# - Se já passou do tempo do alistamento:
# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo:

print('========================================            ALISTAMENTO MILITAR            ========================================')
print('---- De acordo com nossas diretrizes se voçê tem 18 ou mais anos de idade voçê deverá se alistar no exercito brasileiro ----')

ano_nascimento = int(input('Digite aqui em que ano voçê nasceu: '))
idade = 2024 - ano_nascimento
print(f'Voçê nasceu no ano de {ano_nascimento} então voçê tem hoje em dia {idade} anos. ')

if idade < 18:
    alistar = 18 - idade
    print(f'Portanto voçê ainda não pode se alistar mas daqui a {alistar} anos voçê deverá se alistar.')
elif idade == 18:
    print('Portanto está na hora de se alistar no Exercicito Brasileiro.')
elif idade > 18:
    alistar = idade - 18
    print(f'Portanto voçê deveria ter se alistado a pelo menos {alistar} anos atras. Caso não tenha feito, cumpra com o seu dever.')
