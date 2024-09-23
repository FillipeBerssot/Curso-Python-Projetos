# VARIAVEIS COMPOSTAS : 
#   Dicionarios   ---> { }:
#  

# Exemplo 01:
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')

for k, v in pessoas.items():
    print(f'{k} = {v}')

# Exemplo 02:
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ' }
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])

# Exemplo 03:
estado = dict()
brazil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brazil.append(estado.copy())
for e in brazil:
    for v in e.values():
        print(v, end=' ')
    print()