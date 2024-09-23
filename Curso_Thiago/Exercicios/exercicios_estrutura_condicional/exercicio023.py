#Ex.23- Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”:

temperatura_atual = int(input("Qual a temperatura atual? "))

if temperatura_atual <= 20:
    print(f'A temperatura de {temperatura_atual}° é considerado "frio"')
elif temperatura_atual >= 30:
    print(f'A temperatura de {temperatura_atual}° é considerado "quente"')
else:
    print(f'A temperatura de {temperatura_atual}° é considerado "agradavel"')
