# Consulta de CEP e Consulta de COTACOES
#  Na API DE COTACOES utilizar somente o Retorna moedas selecionadas (atualizado a cada 30 segundos)
#  E Retorna o fechamento dos últimos dias e na API de CEP Buscar um CEP:
#  É obrigatório Utilizar Classe e Herança de classe
#  Biblioteca Requests
#  O código das moedas deve ser de acordo com o que a Api fornece

import requests


class BaseAPI:
    def get(self, url, **kwargs):
        response = requests.get(url, **kwargs)
        return response.json() if response.status_code == 200 else None


class CepAPI(BaseAPI):
    def consultar(self, cep):
        url = f'https://cep.awesomeapi.com.br/json/{cep}'
        return self.get(url)

    validar_cep = lambda self, cep: len(cep) == 8 and cep.isdigit()


class CotacaoAPI(BaseAPI):
    def consultar(self, moedas):
        url = f'https://economia.awesomeapi.com.br/json/last/{moedas}'
        return self.get(url)

    def consultar_fechamento(self, moeda):
        url = f'https://economia.awesomeapi.com.br/json/daily/{moeda}/10'
        return self.get(url)

class ExibicaoDados:
    def exibir_cep(self, resultado):
        print("\n--- Informações do CEP ---")
        print(f"CEP: {resultado.get('cep', 'Não informado')}")
        print(f"Endereço: {resultado.get('address', 'Não informado')}, {resultado.get('district', 'Não informado')}")
        print(f"Cidade: {resultado.get('city', 'Não informado')}, Estado: {resultado.get('state', 'Não informado')}")
        print(f"DDD: {resultado.get('ddd', 'Não informado')}")
        print(f"Latitude: {resultado.get('lat', 'Não informado')}, Longitude: {resultado.get('lng', 'Não informado')}")
        print(f"IBGE: {resultado.get('city_ibge', 'Não informado')}")
        print("-------------------------\n")

    def exibir_cotacao(self, resultado):
        print("\n--- Cotações de Moedas ---")
        for moeda, info in resultado.items():
            print(f"Moeda: {info.get('name', 'Não informado')}")
            print(f"Compra: {info.get('bid', 'Não informado')}")
            print(f"Venda: {info.get('ask', 'Não informado')}")
            print(f"Máxima: {info.get('high', 'Não informado')}")
            print(f"Mínima: {info.get('low', 'Não informado')}")
            print(f"Variação: {info.get('pctChange', 'Não informado')}%")
            print("-------------------------\n")

    def exibir_fechamento(self, resultado):
        print("\n--- Fechamento dos últimos dias ---")
        for dia in resultado:
            print(f"Data: {dia.get('create_date', 'Não informado')}")
            print(f"Máxima: {dia.get('high', 'Não informado')}")
            print(f"Mínima: {dia.get('low', 'Não informado')}")
            print(f"Compra: {dia.get('bid', 'Não informado')}")
            print(f"Venda: {dia.get('ask', 'Não informado')}")
            print("-------------------------\n")

class SistemaConsulta(BaseAPI):
    def executar(self):
        cep_api = CepAPI()
        cotacao_api = CotacaoAPI()
        exibicao = ExibicaoDados()

        while True:
            print("Bem-vindo ao sistema de consulta de CEP e cotações de moedas.")
            print("1 - Consultar CEP")
            print("2 - Consultar cotações de moedas")
            print("3 - Consultar fechamento de moeda")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                while True:
                    cep = input("Digite o CEP (somente números, 8 dígitos): ")
                    if cep_api.validar_cep(cep):
                        resultado = cep_api.consultar(cep)
                        if resultado and 'cep' in resultado:
                            print("Resultado do CEP:")
                            exibicao.exibir_cep(resultado)
                        else:
                            print("CEP inválido ou não encontrado.")
                        break
                    else:
                        print('CEP inválido. Tente novamente.\n')

            elif opcao == '2':
                moedas = input("Digite os códigos das moedas (ex: USD-BRL, EUR-BRL, BTC-BRL): ")
                resultado = cotacao_api.consultar(moedas)
                if resultado:
                    print("Resultado das Cotações:")
                    exibicao.exibir_cotacao(resultado)
                else:
                    print("Moeda inválida. Tente novamente.\n")

            elif opcao == '3':
                moeda = input("Digite o código da moeda (ex: USD-BRL, EUR-BRL, BTC-BRL): ")
                resultado = cotacao_api.consultar_fechamento(moeda)
                if resultado:
                    print("Fechamento da moeda:")
                    exibicao.exibir_fechamento(resultado)
                else:
                    print("Moeda inválida ou erro ao consultar o fechamento. Tente novamente.\n")

            elif opcao == '0':
                print("\nFechando o sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.\n")


sistema = SistemaConsulta()
sistema.executar()

