# Ex.013 - Faça um programa para validar o login de um usuario: 

def validar_usuario_senha(login_usuario, senha_usuario):

    while True:
        if login_usuario == usuario['Login'] and senha_usuario == usuario['Senha']:
            print('Login Validado com Sucesso.')
            break
        else:
            print('Login ou Senha Incorreto. Por favor, digite novamente.')
            login_usuario = input('\nValide aqui o seu Login novamente: ')
            senha_usuario = input('Valide agora a sua Senha novamente: ')


usuario = {}
print('Crie um Login e uma Senha: ')
        
usuario['Login'] = input('\nDigite aqui o login que deseja utilizar: ')
usuario['Senha'] = input('Digite agora a senha que deseja utilizar: ')

login_usuario = input('\nValide aqui o seu Login criado: ')
senha_usuario = input('Valide agora a sua Senha criada: ')

validar_usuario_senha(login_usuario, senha_usuario)