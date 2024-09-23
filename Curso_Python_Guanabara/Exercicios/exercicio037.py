# Desafio 037- Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão:
# 1 para binario:
# 2 para octal:
# 3 para hexadecimal:

numero = int(input('Digite aqui um numero inteiro e converta ele para as seguintes conversões: '))
print('Digite 1 para converter para BINARIO: ')
print('Digite 2 para converter para OCTAL: ')
print('Digite 3 para converter para HEXADECIMAL: ')
escolha = int(input('Digite aqui a sua escolha 1 , 2 ou 3: '))

if escolha == 1:
    numero_binario = bin(numero)                                                                    # bin(numero)  --> conversao automatica para BINARIO
    print(f'O numero digitado {numero} convertido para BINARIO é {numero_binario[2:]}')
elif escolha == 2:   
    numero_octal = oct(numero)                                                                      # oct(numero)  --> conversao automatica para OCTAL
    print(f'O numero digitado {numero} convertido para OCTAL é {numero_octal[2:]}')
elif escolha == 3:
    numero_hexadecimal = hex(numero)                                                                # hex(numero)  --> conversao automatica para HEXADECIMAL
    print(f'O numero digitado {numero} convertido para HEXADECIMAL é {numero_hexadecimal[2:]}')
else:
    print('Digite uma opção coreta (1 , 2 ou 3) por favor.')