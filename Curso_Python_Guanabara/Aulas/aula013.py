# Estrutura de repeticao com variavel de controle, FOR: 
for c in range(0, 6):
    print('Oi')
print('Fim')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1 ,p):
    print(c)
print('FIM')

s = 0
for c in range(0,3):
    n = int(input('Digite aqui um valor: '))
    s += n
print(f'A soma de todos os valores digitados é {s}.')
print('FIM')

# Exemplo pratico de for:
''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
 A soma da idade do grupo: FEITO
 A média de idade do grupo: FEITO
 Qual o nome do homem mais velho do grupo:FEITO 
 Quantos homens tem no grupo: FEITO
 Quantas mulheres têm menos de 20 anos do grupo: FEITO
 Qual o nome das mulheres que tem mais de 20 anos do grupo: FEITO
 Quantas mulheres tem no grupo:FEITO '''

lista_pessoas = []

for c in range(1,5):
    nome = input(f'Digite aqui o nome da pessoa {c}: ').strip().capitalize()
    idade = int(input(f'Digite agora a idade da pessoa {c}: '))
    sexo = input(f'Digite agora o sexo da pessoa {c}: ')

    pessoa = {'nome': nome, 'idade': idade, 'sexo': sexo}
    lista_pessoas.append(pessoa)

# Soma e media das idades do grupo:
lista_de_idades = []
for pessoa in lista_pessoas:
    lista_de_idades.append(pessoa['idade'])

soma_das_idades = sum(lista_de_idades)
media_das_idades = sum(lista_de_idades) / len(lista_de_idades)
print(f'A soma das idades do grupo definido é {soma_das_idades}')
print(f'A media das idades do grupo definido é {media_das_idades}')

# Quantos homens e quantas mulheres tem no grupo:
lista_de_homens = 0
lista_de_mulheres = 0
for pessoa in lista_pessoas:
    if pessoa['sexo'] == 'f':
        lista_de_mulheres += 1
for pessoa in lista_pessoas:
    if pessoa['sexo'] == 'm':
        lista_de_homens += 1
print(f'A quantidade de mulheres no grupo definido é {lista_de_mulheres}')
print(f'A quantidade de homens no grupo definido é {lista_de_homens}')

# Qual o nome do homem mais velho do grupo:
maior_idade = 0

for pessoa in lista_pessoas:
    if pessoa['idade'] > maior_idade and pessoa['sexo'] == 'm':
        maior_idade = pessoa['idade']
        homem_mais_velho = pessoa
print(f'O nome do homem mais velho do grupo definido é o {homem_mais_velho['nome']} com {homem_mais_velho['idade']} anos.') 

# Quantas mulheres têm menos de 20 anos do grupo: 

mulheres_com_menos_de_20_anos = 0
for pessoa in lista_pessoas:
    if pessoa['sexo'] == 'f' and pessoa['idade'] < 20:
        mulheres_com_menos_de_20_anos += 1
        
print(f'A quantidade de mulheres que tem menos de 20 anos no grupo definido é {mulheres_com_menos_de_20_anos}.')

# Qual o nome das mulheres que tem mais de 20 anos do grupo:
nome_mulheres_com_mais_de_20_anos = list()
for pessoa in lista_pessoas:
    if pessoa['sexo'] == 'f' and pessoa['idade'] > 20:
        nome_mulheres_com_mais_de_20_anos.append(pessoa['nome'])

print(f'O nome das mulheres no grupo definido com mais de 20 anos é {nome_mulheres_com_mais_de_20_anos}')