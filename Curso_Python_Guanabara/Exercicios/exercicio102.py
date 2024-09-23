# Ex.102- Crie um programa que tenha um função fatorial() que receba dois parametros: o primeiro que indique o numero a calcular
# e o outro chamado show, que será um valor logico(opcional) indicando se será mostrado ou não na tela o processo de calculo fatorial:

def fatorial(numero, show=False):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
    return f


print('-' * 30)
print(fatorial(5, False))
print('-' * 30)
print(fatorial(5, True))
