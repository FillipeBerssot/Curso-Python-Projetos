# Ex.061 - Refaça o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while:

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro_termo
contador = 1

print("Os 10 primeiros termos da Progressão Aritmética são:")

while contador <= 10:
    print(f"{termo_atual}", end=" -> " if contador < 10 else " -> Fim\n")
    termo_atual += razao
    contador += 1
