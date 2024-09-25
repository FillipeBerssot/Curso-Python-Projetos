# Ex.016 - Utilize o if e assert para criar um teste unitario para sua calculadora:

def calculadora_simples(numero01,numero02,operacao):
    if operacao == '+':
        resultado = numero01 + numero02
    elif operacao == '-':
        resultado = numero01 - numero02
    elif operacao == '*':
        resultado = numero01 * numero02
    elif operacao == '/':
        if numero02 != 0:
            resultado = numero01 / numero02
        else:
            return 'Divisão por zero não é permitida.'
     
    else:
        return 'Operação Inválida.'
          
    return resultado


def teste_calculadora():
    assert calculadora_simples(10, 5, '+') == 15
    assert calculadora_simples(10, 5, '-') == 5
    assert calculadora_simples(10, 5, '*') == 50
    assert calculadora_simples(10, 5, '/') == 2
    assert calculadora_simples(10, 0, '/') == 'Divisão por zero não é permitida.'
    print('Todos os testes passaram!')

teste_calculadora()
