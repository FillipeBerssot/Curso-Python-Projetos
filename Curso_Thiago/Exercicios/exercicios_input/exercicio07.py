# 07- Solicite ao usuário que insira uma string e imprima ela invertida e em maiúsculas:

string_inserida_pelo_usuario = input("Digite aqui qualquer mensagem: ")
string_inserida_pelo_usuario_invertida = string_inserida_pelo_usuario[::-1]
#print(string_inserida_pelo_usuario_invertida)

string_inserida_pelo_usuario_invertida_maiusculo = string_inserida_pelo_usuario_invertida.upper()
#print(string_inserida_pelo_usuario_invertida_maiusculo)
print(f"A mensagem digitada será exibida invertida e em maiusculo: {string_inserida_pelo_usuario_invertida_maiusculo}")       #[::-1], -1 é o ultimo caractere do valor da variavel, retornando ele em primeiro
