# Desafio 040- Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - A vista no dinheiro ou cheque: 10% de desconto
# - A vista no cartão de credito: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

print('-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=   Bem Vindo a Loja   =-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('                        Estamos com desconto nos nossos produtos, Aproveite!                           ')
print('                          A vista no dinheiro ou cheque: 10% de desconto                               ')
print('                           A vista no cartão de credito: 5% de desconto                                ')
print('                               Em até 2x no cartão: Preço normal                                       ')
print('                               3x ou mais no cartão: 20% de juros                                      ')
print('-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=')

valor_produto = float(input('Digite aqui o valor a ser pago pelo produto R$: '))

print(f'O produto desejado é R$: {valor_produto}, qual a forma de pagamento:')
print('Digite 1 para À Vista no Dinheiro ou Cheque')
print('Digite 2 para À Vista no Cartão de Crédito')
print('Digite 3 para 2x no Cartão de Crédito')
print('Digite 4 para 3x ou mais no Cartão de Crédito')
opcao = int(input('Digite aqui sua opção (1, 2, 3, ou 4): '))

if opcao == 1:
    novo_valor_produto = valor_produto - (valor_produto * 0.10)
    print(f'Pagando à Vista no Dinheiro ou Cheque seu produto sai por R$ {novo_valor_produto}.')
elif opcao == 2:
    novo_valor_produto = valor_produto - (valor_produto * 0.05)
    print(f'Pagando à Vista no Cartão de Crédito seu produto sai por R$ {novo_valor_produto}.')
elif opcao == 3:
    novo_valor_produto = valor_produto
    print(f'Pagando em 2x no Cartão de Crédito não altera o valor do produto desejado, R$ {novo_valor_produto}.')
elif opcao == 4:
    novo_valor_produto = valor_produto + (valor_produto * 0.20)
    print(f'Pagando em 3x ou mais no Cartão de Crédito o seu produto sai por R$ {novo_valor_produto}.')
else:
    print('Digite uma opção correta (1, 2, 3, ou 4).')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=   OBRIGADO PELA PREFERÊNCIA   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=          VOLTE SEMPRE         =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')