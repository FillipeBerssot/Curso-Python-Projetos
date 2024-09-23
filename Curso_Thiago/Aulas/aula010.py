# funções:
# def

# exemplo função soma:
'''def soma(a, b, c):
    soma = a + b
    multiplicacao = a * b
    return soma , multiplicacao

print(soma(a=15, b=25))'''


order_dic = [
    {
        'payment': '',
        'card':'',
        'holder':'Fillipe',
        'card_name':''
    }, 
    {
        'payment': '',
        'card': '',
        'holder': 'Thiago',
        'card_name': ''
    }
]

for valores in order_dic:
    valores['payment']= 'Pagamento realizado'
    valores['card'] = 'Cartao de Credito'
    if valores['holder'] == 'Fillipe':
        valores['payment']= 'Pagamento realizado'
        valores['card_name'] = 'Fillipe'
        valores['cvc'] = '363'
        valores['data_de_validade'] = '10/37'
        valores['bandeira'] = 'MASTERCARD'
    elif valores['holder'] == 'Thiago':
        valores['card_name'] = 'Thiago'
        valores['cvc'] = '484'
        valores['data_de_validade'] = '01/42'
        valores['bandeira'] = 'VISA'

print(order_dic)

# Adicionar para cada cartão o CVC de 3 dígitos, 
# Adicionar o tipo de bandeira (MASTECARD, ELO, VISA), 
# Adicionar data de validade no formato (MM/AA), sendo que para o usuário 1 o CVC tem que ser : 363 e pro usuário 2 : 484, 
# a data de validade pro usuario 1: 10/37 e para o usuário 2: 01/42

