# Desafio 036- Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacão mensal sabendo que ela não pode exceder 30% do salario ou entao o emprestimo sera negado:

print('-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-   Bem Vindo ao Banco Santo André    -//-//-//-//-//-//-//-//-//-//-//-//-')
print('-//-//-//-//-//-//-//-//-//-//-//-//-    Bem Vindo ao Programa de Emprestimo Bancario    -//-//-//-//-//-//-//-//-//-//-')

valor_casa = float(input('Digite aqui o valor total da casa que voçê deseja: '))
print(f"O valor da casa deseja é R$: {valor_casa}.")

salario = float(input('Digite agora o seu salario atual para sabermos se voçê pode ou não receber o emprestimo: '))
print(f'Seu salario atual é de R$: {salario}.')

anos = float(input('Digite agora em quantos anos voçê deseja pagar o emprestimo desejado: '))
print(f'De acordo com o que foi digitado, voçê quer parcelar a casa em exatamente {anos:.0f} meses.')

print('-//-//-//-//-//-//-//-//-//-//-//--//-//-//-//-//-//-//-//-//-//-//--//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-')
prestacão_mensal = valor_casa / (anos * 12)
print(f'O valor da prestação mensal do seu emprestimo será de R$: {prestacão_mensal:.2f} em {anos:.0f} anos.')

if prestacão_mensal <= salario * 0.30:
    print(f'De acordo com o seu salario, voçê atingiu as especificações do banco para aprovar o seu emprestimo. PARABENS!')
else:
    print(f'De acordo com o seu salario, voçê não atingiu as especificações do banco para aprovar o seu emprestimo. SINTO MUITO.')

print('-//-//-//-//-//-//-//-//-//-//-//--//-//-//-//-//-//-//-//-//-//-//--//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-')