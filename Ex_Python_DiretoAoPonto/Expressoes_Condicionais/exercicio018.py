# Ex.018 - Faça um programa para verificar se um cliente está apto a receber emprestimo. O nome dele deve estar limpo, 
# ele deve ganhar mais que 5000 e ele deve ter mais de 18 anos:

def verificar_emprestimo(opcao_nome_limpo, salario=None, idade=None):
    if opcao_nome_limpo == 1:
        if salario <= 5000:
            return '\nO seu nome está limpo, mas você não recebe mais de R$5000 por mês. Não podemos dar continuidade ao empréstimo.'
        if idade <= 18:
            return '\nO seu nome está limpo, mas você não tem mais de 18 anos. Não podemos dar continuidade ao empréstimo.'
        return '\nO seu nome está limpo, você recebe mais de R$5000 e tem mais de 18 anos. Podemos dar continuidade ao empréstimo.'
        
    elif opcao_nome_limpo == 2:
        return '\nO seu nome não está limpo. Não podemos dar continuidade ao empréstimo.'
    
    else:
        return 'Opção inválida.'


nome = input('Digite o seu Nome: ').strip().capitalize()
opcao_nome_limpo = int(input('\nDigite 1 se o seu nome está limpo e 2 se não estiver limpo: '))

if opcao_nome_limpo == 1:
    salario = float(input('Digite aqui o seu salário: '))
    idade = int(input('Digite aqui a sua idade atual: '))
    print(verificar_emprestimo(opcao_nome_limpo, salario, idade))

else:
    print(verificar_emprestimo(opcao_nome_limpo))
