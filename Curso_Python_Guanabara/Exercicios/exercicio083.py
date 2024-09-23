# Ex. 083- Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
# Seu aplicativo devera analisar se a expressao passada está com os parenteses abertos e fechados na ordem correta:

# Maneira 01:
expr = input('Digite a expressão: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está Válida!')
else:
    print('Sua expressão está Errada!')

# Maneira 02:
parenteses_abertos_e_fechados = []
expressao = input('Digite aqui qualquer expressao matematica que utilize parenteses: ')

for caracteres in expressao:
    if caracteres == '(':
        parenteses_abertos_e_fechados.append(caracteres)

    elif caracteres == ')':
        if parenteses_abertos_e_fechados:
            parenteses_abertos_e_fechados.pop()
        else:
            parenteses_abertos_e_fechados.append(')')

if not parenteses_abertos_e_fechados:
    print('Expressão Valida. Todos os parenteses estão fechados corretamente.')
else:
    print('Expressão Invalida. Há parenteses não fechados corretamente.')
