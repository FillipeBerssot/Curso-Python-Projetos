# API:

import requests
import pprint

# Verbos de Requisição. (POST/GET/UPDATE/DELETE)
# Vamos utilizar apenas e somente GET (Listar ou Pegar)

cep = input('Digite seu cep: ')
response = requests.get(f'https://viacep.com.br//ws/{cep}/json/')

if response.status_code == 200:
    data = response.json()

pprint.pprint(data)
print(f'bairro: {data['bairro']} // cidade: {data['localidade']}')
