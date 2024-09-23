# Ex. 069- Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, 
# o programa devera perguntar se o usuario quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.: FEITO
# B) Quantos homens foram cadastrados: FEITO
# C) Quantas mulheres tem menos de 20 anos: FEITO

tot18 = 0
totH = 0
totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: ').strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S / N]: ').strip().upper()
    if resp == 'N':
        print('\nFinalizando o Programa. Mostrando as informações abaixo: ')
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')