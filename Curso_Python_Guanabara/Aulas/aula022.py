# Tratamento de ERROS e EXEÇÕES :  
#   Try and Except:

#   try:
#        operação
#   except:
#        falhou
#   else:
#        deu certo
#   finally:
#        certo/falha


# Exemplo 01:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__})')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Obrigado')

# Exemplo 02:
try:
    x = int(input('Numerador:'))
    y = int(input('Denominador: '))
    resultado = x / y
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voçê digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {resultado:.1f}')
finally:
    print('Volte Sempre. Obrigado!')