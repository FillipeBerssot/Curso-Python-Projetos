# Ex. 073- Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados: FEITO
# B) Os ultimos 4 colocados da tabela: FEITO
# C) Uma lista com os times em ordem alfabetica: FEITO
# D) Em que posição na tabela esta o time da Chapecoense: FEITO

primeiros_20_colocados_brasileirao = ('Fortaleza', 'Botafogo', 'Palmeiras', 'Flamengo', 'Sao Paulo', 'Bahia', 'Cruzeiro',
                                      'Vasco', 'Atletico-MG', 'Athletico-PR', 'Internacional', 'Juventude', 'Gremio', 'Bragantino', 'Criciuma',
                                      'Fluminense', 'Chapecoense', 'Vitoria', 'Corinthians', 'Atletico-GO')

print('-=-' * 50)
# A):
print(f'Os 5 primeiros colocados da tabela são: {primeiros_20_colocados_brasileirao[0:5]}')
print('-=-' * 50)

# B):
print(f'Os ultimos 4 colocados da tabela são: {primeiros_20_colocados_brasileirao[-4:]}')
print('-=-' * 50)

# C):
print(f'A tabela com os times em Ordem Alfabetica fica: {sorted(primeiros_20_colocados_brasileirao)}')
print('-=-' * 50)

# D):
print(f'O time da Chapecoense está na {primeiros_20_colocados_brasileirao.index("Chapecoense")+1}º posição')
print('-=-' * 50)
