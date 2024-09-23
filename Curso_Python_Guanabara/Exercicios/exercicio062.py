# Ex.062- Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos:

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro_termo
contador = 1
total_termos = 0
mais_termos = 10

while mais_termos != 0:
    total_termos += mais_termos
    while contador <= total_termos:
        print(f'{termo_atual}', end=' -> ')
        termo_atual += razao
        contador += 1
    print('Pausa')

    mais_termos = int(input('Quantos termos voçê quer mostrar a mais? (Digite 0 para encerrar o programa): '))
print(f'Progessao finalizada com {total_termos} termos mostrados.')