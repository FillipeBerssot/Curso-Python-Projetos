# Ex. 03- Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

print(
    '===================================================================================='
)

nome = input('Digite o seu nome: ')
# validação:
while len(nome) <= 3:
    print(
        'O Nome inserido é Inválido. Nome deve conter mais do que 3 caracteres.'
    )
    nome = input('Digite o seu nome novamente: ')
print('O Nome inserido é Válido.')

print(
    '===================================================================================='
)

idade = int(input('Digite a sua idade: '))
# validaçao:
while idade <= 0 or idade > 150:
    print('A Idade inserida Inválida. Insira uma idade entre 0 e 150.')
    idade = int(input('Digite a sua idade novamente: '))
print('A Idade inserida é Válida.')

print(
    '===================================================================================='
)

salario = float(input('Digite o seu salario atual:'))
# validação:
while salario <= 0:
    print('O Salario inserido é Inválido. Salario deve ser maior do que zero.')
    salario = float(input('Digite o seu salario atual novamente: '))
print('Salario inserido é Válido.')

print(
    '===================================================================================='
)

print('Digite a opção para o seu genero: ')
print('[f] para Feminino')
print('[m] para masculino')
genero = input(' ')
# validação:
while genero != 'f' and genero != 'm':
    print('A Opção inserida é Inválida.')
    genero = input('Digite novamente uma opção entre [f] ou [m]. ')
print('A Opção inserida é Válida.')

print(
    '===================================================================================='
)

print('Digite a opção para o seu Estado Civil: ')
print('[s] para Solteiro(a)')
print('[c] para Casado(a)')
print('[v] para Viúvo(a)')
print('[d] para Divorciado(a)')
estado_civil = input(' ')
# validaçao:
while (
    estado_civil != 's'
    and estado_civil != 'c'
    and estado_civil != 'v'
    and estado_civil != 'd'
):
    print('A Opção inserida é Inválida.')
    estado_civil = input(
        'Digite novamente uma opção entre [s], [c], [v], [d]. '
    )
print('A Opção inserida é Válida.')

print(
    '===================================================================================='
)

print('De acordo com os valores e opções inseridos:')
print(f'Seu nome é {nome}.')
print(f'Voçê tem {idade} anos.')
print(f'Seu sálario atual é de R$: {salario}')

if estado_civil == 's':
    print('O seu Estado Civil é Solteiro(a)')
elif estado_civil == 'c':
    print('O seu Estado Civil é Casado(a)')
elif estado_civil == 'v':
    print('O seu Estado Civil é Viuvo(a)')
elif estado_civil == 'd':
    print('O seu Estado Civil é Divorciado(a)')

if genero == 'f':
    print('O seu genero é Feminino.')
elif genero == 'm':
    print('O seu genero é Masculino.')
print(
    '===================================================================================='
)
