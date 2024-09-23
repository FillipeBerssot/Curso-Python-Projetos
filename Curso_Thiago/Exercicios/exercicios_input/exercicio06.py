# 06- Solicite ao usuário que insira uma frase e imprima ela com todos os espaços substituídos por "_" e que essa frase esteja toda em maiúsculo.

string_do_usuario = input("Digite aqui qualquer mensagem: ")
#print(string_do_usuario)

string_do_usuario_substituido = string_do_usuario.replace(" ", "_")
#print(string_do_usuario_substituido)

string_do_usuario_maiusculo = (string_do_usuario_substituido.upper())
#print(string_do_usuario_maiusculo)

print(f'A mensagem digita será exibida trocando todos os "espaços" por "_" e deixando a frase toda em maiusculo: {string_do_usuario_maiusculo}')
