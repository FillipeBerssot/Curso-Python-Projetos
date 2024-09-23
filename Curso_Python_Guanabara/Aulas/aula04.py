# 1° desafio: 

# nome = input("Qual o seu nome? ")
# nome = nome.capitalize()
# print(f"Olá {nome}! Seja muito bem vindo ao Python 3!")

# 2° desafio:

# dia_aniversario = input("Digite o dia em que voçê nasce: ")
# mes_aniversario = input("Digite agora o mês em que voçê nasceu: ")
# ano_aniversario = input("Digite agora o ano em que voçê nasceu: ")

# print(f"Voçê nasceu no dia {dia_aniversario} no mês {mes_aniversario} e no ano de {ano_aniversario}.")

# 3° desafio:

# numero1 = int(input("Digite um numero aleatorio: "))
# numero2 = int(input("Digite aqui um outro numero aleatorio: "))
# soma = numero1 + numero2

# print(f"A soma entre os dois numeros digitados é: {soma}.")

# 4° desafio:

# nome = input("Digite algo: ")
# print(f"O tipo primitivo do que foi digitado é: {type(nome)}")
# print(f"O que foi digitado so tem espaços? {nome.isspace()}")
# print(f"O que que foi digitado é numerico? {nome.isnumeric()}")
# print(f"O que foi digitado é alfabetico? {nome.isalpha()}")
# print(f"O que foi digitado é alfanumerico? {nome.isalnum()}")
# print(f"O que foi digitado está em maiusculo? {nome.isupper()}")
# print(f"O que foi digitado está em minusculo? {nome.islower()}")
# print(f"O que foi digitado está capitalizado? {nome.istitle()}")

# nome = input("Digite seu nome ")
# print(f"Ola {nome:>20} seja bem vindo! ")                                 # {nome:20}     ---> dar 20 espacos da variavel
# print(f"Ola {nome:^20} seja bem vindo! ")                                 # {nome:^20}    ---> centralizar e tambem pode colocar qualquer caracteres, ex: {nome:=^20}

# n1 = 3.5
# n2 = 8
# potencia = n1 ** n2 / 4
# print(f"O valor de {potencia:.2f}")                                       # {potencia:.2f}  ---> formatar para ter apenas 2 casas apos a virgula.