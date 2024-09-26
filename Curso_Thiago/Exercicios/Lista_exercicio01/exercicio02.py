# Ex. 02- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# Mostrando uma mensagem de erro e voltando a pedir as informações:
# Solução: Validação de dados em Python

print('-=-=-=-=-=- Faça Aqui o Seu Cadastro -=-=-=-=-=-')
nome_usuario = input('Digite um nome de usuario: ')
senha = input('Digite agora a sua senha: ')

while senha == nome_usuario:
    print('A senha não pode ser igual ao nome de usuario. Digite novamente.')
    senha = input('Digite agora a sua senha: ')
print('Cadastro Efetuado Com Sucesso!')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
