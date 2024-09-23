# CORES NO TERMINAL:
# Codigo ANSI

# \033[ style; text; back]     =     \033[0;33;44m
  
# style --> fundo do terminal
# texto --> cor do texto
# back  --> cor do fundo
 
#    style         |        Text          |          Back       |
#                  |     30 - Branco      |     40 - Branco     |
#   0 - none       |     31 - Vermelho    |     41 - Vermelho   |
#   1 - Bold       |     32 - Verde       |     42 - Verde      |
#   4 - Underline  |     33 - Amarelo     |     43 - Amarelo    |
#   7 - Negative   |     34 - Azul        |     44 - Azul       |
#                  |     35 - Magenta     |     45 - Magenta    |
#                  |     36 - Ciano       |     46 - Ciano      |
#                  |     37 - Cinza       |     47 - Cinza      |

# TESTES:

""" TESTE\033[0;30;41m
TESTE\033[4;33;44m
TESTE\033[1;35;43m
TESTE\033[30;42m
TESTE\033[m
TESTE\033[7;30m """

# Ex 01:

"""print('Olá, Mundo!')
print('\033[0;30;41mOlá, Mundo! Vermelho')
print('\033[4;33;44mOlá, Mundo! Azul')
print('\033[1;35;43mOlá, Mundo! Amarelo')
print('\033[30;42mOlá, Mundo! Verde')
print('\033[7;30mOlá, Mundo! Preto')

print('\033[7;30;41mOlá, Mundo! Vermelho')
print('\033[7;33;44mOlá, Mundo! Azul')
print('\033[7;35;43mOlá, Mundo! Amarelo')
print('\033[7;42mOlá, Mundo! Verde')
print('\033[36;30mOlá, Mundo! Preto')"""

# Ex 02:

nome = 'Fillipe'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;33m'}

print(f"Olá! Muito prazer em te conhecer, {cores['amarelo']} {nome} {cores['limpa']} !!!")
