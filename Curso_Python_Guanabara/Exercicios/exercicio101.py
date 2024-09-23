# Ex. 101- Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATORIO nas eleições:
# + 65 voto opcional, + 18 voto obrigatorio, - 18 voto negado:

# Maneira 01:
def voto01(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'
    

nasc = int(input('Em que ano voçê nasceu? '))
print(voto01(nasc))

# Maneira 02:
def voto(nascimento):
    idade = 2024 - nascimento
    if 0 < idade < 16:
        print(f'VOTO NEGADO. Voçê tem apenas {idade} anos')
    elif 16 <= idade < 18 or idade > 65:
        print(f'VOTO OPCIONAL. Voçê tem {idade} anos')
    else:
        print(f'VOTO OBRIGATORIO. Voçê tem {idade} anos')


print('-' * 88)
ano_nascimento = int(input('Digite o ano de nascimento e saiba se o seu voto é OBRIGATORIO, NEGADO ou OPCIONAL: '))
voto(ano_nascimento)
