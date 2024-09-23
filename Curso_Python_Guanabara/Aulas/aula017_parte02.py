# VARIAVEIS COMPOSTAS :
#   CONTINUAÇÃO ---> LISTAS: [ ]
#       Listas compostas:

# Exemplo 01:
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# Exemplo 02:
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

# Exemplo 03:
galera02 = list()
dados = list()
total_maior = 0
total_menor = 0
for c in range(0,3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera02.append(dados[:])
    dados.clear()
for p in galera02:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1
print(f'Temos {total_maior} maiores de idade e {total_menor} menores de idade.')

