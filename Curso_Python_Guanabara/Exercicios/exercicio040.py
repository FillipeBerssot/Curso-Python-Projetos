# Desafio 040- Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
# - Media abaixo de 5.0: Reprovado
# - Media entre 5.0 e 6.9: Recuperação
# - Media 7.0 ou superior: Aprovado


print('==============================     Escola Javali    ==============================')
print('Média abaixo de 5.0 => Reprovado')
print('Média entre 5.0 e 6.9 => Recuperação')
print('Média 7.0 ou Superior => Aprovado')
print('Descubra aqui qual foi sua Média')
print('==================================================================================')

nota01 = float(input('Digite aqui a sua primeira nota (N1): '))
nota02 = float(input('Digite agora a sua segunda nota (N2): '))
print(f"De acordo com o que foi informado sua N1 = {nota01} e sua N2 = {nota02}.")

media = (nota01 + nota02) / 2
print(f'Então sua Média é = {media}.')

print('==================================================================================')

if media < 5:
    print('Voçê foi REPROVADO. Sinto Muito.')
elif media >= 5 and media <= 6.9:
    print('Voçê está de RECUPERAÇÃO. Boa Sorte.')
else:
    print('Voçê foi APROVADO. Parabéns!!!')