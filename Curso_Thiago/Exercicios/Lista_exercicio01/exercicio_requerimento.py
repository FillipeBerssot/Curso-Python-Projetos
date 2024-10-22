# Consulta de CEP e Consulta de COTACOES
#  Na API DE COTACOES utilizar somente o Retorna moedas selecionadas (atualizado a cada 30 segundos)
#  E Retorna o fechamento dos últimos dias e na API de CEP Buscar um CEP:
#  É obrigatório Utilizar Classe e Herança de classe
#  Biblioteca Requests
#  O código das moedas deve ser de acordo com o que a Api fornece


# import requests


# class BaseAPI:
#     def get(self, url, **kwargs):
#         response = requests.get(url, **kwargs)
#         return response.json() if response.status_code == 200 else None


# class CepAPI(BaseAPI):
#     def consultar(self, cep):
#         url = f'https://cep.awesomeapi.com.br/json/{cep}'
#         return self.get(url)

#     validar_cep = lambda self, cep: len(cep) == 8 and cep.isdigit()


# class CotacaoAPI(BaseAPI):
#     def consultar(self, moedas):
#         url = f'https://economia.awesomeapi.com.br/json/last/{moedas}'
#         return self.get(url)

#     def consultar_fechamento(self, moeda):
#         url = f'https://economia.awesomeapi.com.br/json/daily/{moeda}/10'
#         return self.get(url)

# class ExibicaoDados:
#     def exibir_cep(self, resultado):
#         print("\n--- Informações do CEP ---")
#         print(f"CEP: {resultado.get('cep', 'Não informado')}")
#         print(f"Endereço: {resultado.get('address', 'Não informado')}, {resultado.get('district', 'Não informado')}")
#         print(f"Cidade: {resultado.get('city', 'Não informado')}, Estado: {resultado.get('state', 'Não informado')}")
#         print(f"DDD: {resultado.get('ddd', 'Não informado')}")
#         print(f"Latitude: {resultado.get('lat', 'Não informado')}, Longitude: {resultado.get('lng', 'Não informado')}")
#         print(f"IBGE: {resultado.get('city_ibge', 'Não informado')}")
#         print("-------------------------\n")

#     def exibir_cotacao(self, resultado):
#         print("\n--- Cotações de Moedas ---")
#         for info in resultado.values():
#             print(f"Moeda: {info.get('name', 'Não informado')}")
#             print(f"Compra: {info.get('bid', 'Não informado')}")
#             print(f"Venda: {info.get('ask', 'Não informado')}")
#             print(f"Máxima: {info.get('high', 'Não informado')}")
#             print(f"Mínima: {info.get('low', 'Não informado')}")
#             print(f"Variação: {info.get('pctChange', 'Não informado')}%")
#             print("-------------------------\n")

#     def exibir_fechamento(self, resultado):
#         print("\n--- Fechamento dos últimos dias ---")
#         for dia in resultado:
#             print(f"Data: {dia.get('create_date', 'Não informado')}")
#             print(f"Máxima: {dia.get('high', 'Não informado')}")
#             print(f"Mínima: {dia.get('low', 'Não informado')}")
#             print(f"Compra: {dia.get('bid', 'Não informado')}")
#             print(f"Venda: {dia.get('ask', 'Não informado')}")
#             print("-------------------------\n")

# class SistemaConsulta(BaseAPI):
#     def executar(self):
#         cep_api = CepAPI()
#         cotacao_api = CotacaoAPI()
#         exibicao = ExibicaoDados()

#         while True:
#             print("Bem-vindo ao sistema de consulta de CEP e cotações de moedas.")
#             print("1 - Consultar CEP")
#             print("2 - Consultar cotações de moedas")
#             print("3 - Consultar fechamento de moeda")
#             print("0 - Sair")
#             opcao = input("Escolha uma opção: ")

#             if opcao == '1':
#                 while True:
#                     cep = input("Digite o CEP (somente números, 8 dígitos): ")
#                     if cep_api.validar_cep(cep):
#                         resultado = cep_api.consultar(cep)
#                         if resultado and 'cep' in resultado:
#                             print("Resultado do CEP:")
#                             exibicao.exibir_cep(resultado)
#                         else:
#                             print("CEP inválido ou não encontrado.")
#                         break
#                     else:
#                         print('CEP inválido. Tente novamente.\n')

#             elif opcao == '2':
#                 moedas = input("Digite os códigos das moedas (ex: USD-BRL, EUR-BRL, BTC-BRL): ")
#                 resultado = cotacao_api.consultar(moedas)
#                 if resultado:
#                     print("Resultado das Cotações:")
#                     exibicao.exibir_cotacao(resultado)
#                 else:
#                     print("Moeda inválida. Tente novamente.\n")

#             elif opcao == '3':
#                 moeda = input("Digite o código da moeda (ex: USD-BRL, EUR-BRL, BTC-BRL): ")
#                 resultado = cotacao_api.consultar_fechamento(moeda)
#                 if resultado:
#                     print("Fechamento da moeda:")
#                     exibicao.exibir_fechamento(resultado)
#                 else:
#                     print("Moeda inválida ou erro ao consultar o fechamento. Tente novamente.\n")

#             elif opcao == '0':
#                 print("\nFechando o sistema...")
#                 break
#             else:
#                 print("Opção inválida. Tente novamente.\n")


# sistema = SistemaConsulta()
# sistema.executar()

import xml.etree.ElementTree as ET

import requests


class CEP:
    def __init__(self):
        self.__base_url = 'https://cep.awesomeapi.com.br/json'

    def consultar_cep(self, cep):
        url = f'{self.__base_url}/{cep}'
        requisicao = requests.get(url)
        return requisicao

    def exibir_info_cep(self, cep):
        requisicao = self.consultar_cep(cep)
        if requisicao.status_code == 200:
            resultado = requisicao.json()
            print('\n--- Informações do CEP ---')
            print(f"CEP: {resultado.get('cep', 'Não informado')}")
            print(
                f"Endereço: {resultado.get('address', 'Não informado')}, {resultado.get('district', 'Não informado')}"
            )
            print(
                f"Cidade: {resultado.get('city', 'Não informado')}, Estado: {resultado.get('state', 'Não informado')}"
            )
            print(f"DDD: {resultado.get('ddd', 'Não informado')}")
            print(
                f"Latitude: {resultado.get('lat', 'Não informado')}, Longitude: {resultado.get('lng', 'Não informado')}"
            )
            print(f"IBGE: {resultado.get('city_ibge', 'Não informado')}")
            print('-------------------------\n')
        else:
            message = requisicao.json().get('message', 'Erro desconhecido.')
            print(f'{message}\n')


class Cotacao:
    def verificao_pares_espaco(self, pares_salvos, espaco):
        if len(espaco) > 1:
            print('\nEspaço entre os pares não são permitidos\n')
            return False
        if len(pares_salvos) > 2:
            print('\nLimite de pares excedido\n')
            return False
        else:
            return pares_salvos

    def __init__(self):
        self.__base_url = 'https://economia.awesomeapi.com.br/json'

    def consultar_cotacao(self, moedas):
        url = f'{self.__base_url}/last/{moedas}'
        requisicao = requests.get(url)
        return requisicao

    def validar_dias(self, dias):
        if dias.isnumeric() and int(dias) > 90:
            print('\nO limite de dias é no máximo 90!\n')
            return False
        elif dias.isnumeric() == False:
            print('\nDias só são permitidos como números inteiros\n')
            return False
        else:
            return str(dias)

    def consultar_fechamento(self, moeda, dias):
        url = f'{self.__base_url}/daily/{moeda}/{dias}'
        requisicao = requests.get(url)
        return requisicao

    @staticmethod
    def exibir_pares():
        url = 'https://economia.awesomeapi.com.br/xml/available'

        response = requests.get(url)

        if response.status_code == 200:
            xml_content = response.content

            tree = ET.ElementTree(ET.fromstring(xml_content))

            root = tree.getroot()
            print('')
            for child in root:
                print(child.tag, child.text)
            print('')
        else:
            print(f'Erro: {response.status_code}')

    def exibir_cotacao(self, moedas, pares_salvos, espaco):
        verificao_pares = self.verificao_pares_espaco(pares_salvos, espaco)
        if verificao_pares:
            requisicao = self.consultar_cotacao(moedas)
            if requisicao.status_code == 200:
                resultado = requisicao.json()
                print('\n--- Cotações de Moedas ---')
                for info in resultado.values():
                    print(f"Moeda: {info.get('name', 'Não informado')}")
                    print(f"Compra: {info.get('bid', 'Não informado')}")
                    print(f"Venda: {info.get('ask', 'Não informado')}")
                    print(f"Máxima: {info.get('high', 'Não informado')}")
                    print(f"Mínima: {info.get('low', 'Não informado')}")
                    print(
                        f"Variação: {info.get('pctChange', 'Não informado')}%"
                    )
                    print('-------------------------\n')
            else:
                message = requisicao.json().get(
                    'message', 'Erro desconhecido.'
                )
                print(f'{message}\n')

    def exibir_fechamento(self, moeda, dias):
        limite_dias = self.validar_dias(dias)
        if limite_dias:
            requisicao = self.consultar_fechamento(moeda, dias)
            if requisicao.status_code == 200:
                print('\n--- Fechamento dos últimos dias ---')
                resultado = requisicao.json()
                for dia in resultado:
                    print(f"Data: {dia.get('create_date', 'Não informado')}")
                    print(f"Máxima: {dia.get('high', 'Não informado')}")
                    print(f"Mínima: {dia.get('low', 'Não informado')}")
                    print(f"Compra: {dia.get('bid', 'Não informado')}")
                    print(f"Venda: {dia.get('ask', 'Não informado')}")
                    print('-------------------------\n')
            else:
                print(
                    'Moeda inválida. Tente novamente.\n'
                )

class SistemaConsulta(CEP, Cotacao):
    def __init__(self):
        CEP.__init__(self)
        Cotacao.__init__(self)

    @staticmethod
    def cabecalho():
        print('Bem-vindo ao sistema de consulta de CEP e cotações de moedas.')
        print('1 - Consultar CEP')
        print('2 - Consultar cotações de moedas')
        print('3 - Consultar fechamento de moeda')
        print('4 - Consutar pares de moedas possiveis')
        print('0 - Sair')
        opcao = input('Escolha uma opção: ')

        return opcao

    def executar(self):
        while True:
            opcao = self.cabecalho()
            if opcao == '1':
                while True:
                    cep = input('Digite o CEP (somente números, 8 dígitos): ')
                    self.exibir_info_cep(cep)
                    break
            elif opcao == '2':
                print('\nPossivel fazer com no maximo nove pares de moeda')
                print('Caso colocar mais de dois pares não colocar espaço após a virgula!\n')
                moedas = input(
                    'Digite os códigos das moedas (ex: USD-BRL,EUR-BRL,BTC-BRL): '
                )
                pares_salvos = moedas.split(',')
                espaco = moedas.split(' ')
                self.exibir_cotacao(moedas, pares_salvos, espaco)

            elif opcao == '3':
                moeda = input('Digite o código da moeda (ex: USD-BRL): ')
                dias = input(
                    'Digite o número de dias a partir dos quais você quer o fechamento(limite 90): '
                ).strip()
                self.exibir_fechamento(moeda, dias)

            elif opcao == '4':
                self.exibir_pares()

            elif opcao == '0':
                print('\nFechando o sistema...')
                break
            else:
                print('Opção inválida. Tente novamente.\n')


SistemaConsulta().executar()
