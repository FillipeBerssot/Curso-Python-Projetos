import  json
import re


def menu():
    while True:
        opcao = input('''
======================================================================================
                          .:PROJETO AGENDA EM PYTHON:.
======================================================================================
MENU:
      
[1] .:CADASTRAR CONTATO:.
[2] .:LISTAR CONTATO:.
[3] .:DELETAR CONTATO:.
[4] .:BUSCAR CONTATO POR NOME:.
[5] .:ENCERRAR PROGRAMA.:
                  
ESCOLHA SUA OPÇÃO: ''').strip()

        if opcao == '1':
            cadastrarContato()
        elif opcao == '2':
            listarContato()
        elif opcao == '3':
            deletarContato()
        elif opcao == '4':
            buscarContatoPeloNome()
        elif opcao == '5':
            sair()
        else:
            print('Opção inválida. Tente novamente.')

# operacoes:
def cadastrarContato():
    while True:
        nome_contato = input('Escreva o nome do contato: ').strip().capitalize()

        while True:
            telefone_contato = input('Escreva o telefone do contato: ').strip()
            if validar_telefone(telefone_contato):
                break
            else:
                print('Número de telefone inválido. O telefone deve conter de 10 a 11 dígitos.')

        while True:
            email_contato = input('Escreva o e-mail do contato: ').strip()
            if validar_email(email_contato):
                break
            else:
                print('E-mail inválido. Por favor, digite um e-mail válido no formato: " usuario@dominio.com ".')

        try:
            # Abrindo arquivo em modo append
            with open('Agenda.txt', 'a') as agenda:
                dados = {
                    'Nome do Contato': nome_contato,
                    'Telefone do Contato': telefone_contato,
                    'E-mail do Contato': email_contato
                }
                # Gravando os dados no arquivo como JSON
                agenda.write(json.dumps(dados) + '\n')
            print(f'\nContato gravado com sucesso !!!\n')
        
        except Exception as erro:
            print(f'ERRO na gravação do contato: {erro}')
        
        resposta = validar_saida()
        if resposta == 'n':
            print('\nCadastrar contatos foi encerrado. Obrigado!')
            print('======================================================================================')
            break
            

def listarContato():
    while True:
        try:
            with open('Agenda.txt', 'r') as agenda:
                contatos = agenda.readlines()
                if contatos:
                    print('\nContatos Cadastrados:\n')
                    for linha in contatos:
                        # Lendo e convertendo de volta para dicionario
                        contato = json.loads(linha)
                        print(f'Nome: {contato['Nome do Contato']}, Telefone: {contato['Telefone do Contato']}, E-mail: {contato['E-mail do Contato']}')
                else:
                    print('Nenhum contato foi cadastrado na sua agendda.')

        except FileNotFoundError:
            print('Nenhum contato cadastrado.')
        except Exception as erro:
            print(f'Ocorreu um erro: {erro}')

        resposta = validar_saida()
        if resposta == 'n':
            print('\nListar contato foi encerrado. Obrigado!')
            print('======================================================================================')
            break
            

def deletarContato():
    while True:
        nome_procurado = input('\nDigite o Nome do contato que voçê deseja deletar de sua agenda: ').strip().lower()

        try:
            with open('Agenda.txt', 'r') as agenda:
                contatos = agenda.readlines()

            contatos_atualizados = []
            contato_encontrado = False
            nome_real = ''

            for linha in contatos:
                contato = json.loads(linha)
                if contato['Nome do Contato'].lower() != nome_procurado:
                    contatos_atualizados.append(linha)
                else:
                    contato_encontrado = True
                    nome_real = contato['Nome do Contato']
                
            if contato_encontrado:
                with open('Agenda.txt', 'w') as agenda:
                    agenda.writelines(contatos_atualizados)
                print(f'\n{nome_real} foi deletado(a) com sucesso!\n')
                print('Lista de contatos atualizados: ')
                for linha in contatos_atualizados:
                    contato = json.loads(linha)
                    print(f'Nome: {contato['Nome do Contato']}, Telefone: {contato['Telefone do Contato']}, E-mail: {contato['E-mail do Contato']}')
            else:
                print('Nome do contato fornecido não foi encontrado.')

        except FileNotFoundError:
            print('Nenhum contato foi encontrado, o contato não existe na agenda.')

        resposta = validar_saida()
        if resposta == 'n':
            print('\nDeletar contato foi encerrado. Obrigado!')
            print('======================================================================================')
            break
            

def buscarContatoPeloNome():
    while True:
        nome_procurado = input('\nDigite o Nome do contato que voçê deseja buscar: ').strip().lower()

        try:
            with open('Agenda.txt', 'r') as agenda:
                encontrado = False
                for linha in agenda:
                    contato = json.loads(linha)

                    # Verificar se o Nome do contato corresponde ao valor 
                    if  contato['Nome do Contato'].lower() == nome_procurado:
                        print(f'\nContato Encontrado: \nNome: {contato['Nome do Contato']}\nTelefone: {contato['Telefone do Contato']}\nE-mail: {contato['E-mail do Contato']}')
                        encontrado = True
                        break

                # Verifica se o contato foi encontrado ou não      
                if not encontrado:
                    print('Nome do contato fornecido não foi encontrado. Tente novamente.')

        except FileNotFoundError:
            print('Nenhum contato foi encontrado, o arquivo da agenda não existe.')
            break

        resposta = validar_saida()
        if resposta == 'n':
            print('\nBuscar contatos foi encerrado. Obrigado!')
            print('======================================================================================')
            break


# validacoes:
def validar_saida():
    while True:
        resposta = input('Deseja continuar?[s / n]: ').strip().lower()
        if resposta in 'sn':
            return resposta
        else:
            print('Opção inválida. Por favor digite "s" para sim ou "n" para não.')


def validar_telefone(telefone):
    return re.fullmatch(r'^\d{9,11}$', telefone) is not None


def validar_email(email):
    return re.fullmatch(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email) is not None

def sair():
    print('\nEncerrando o Programa "AGENDA". Obrigado e volte sempre!')
    print('======================================================================================')
    exit()
    
def main():
    menu()

main()