#Ex.15- Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não:

print("Estou fudido para aprender programaçâo? ")

print("A) sim")
print("B) A")
print("C) B")
print("D) Todas as alternativas estão corretas.")

resposta = input("Digite aqui a letra da sua resposta (A), (B), (C) ou (D): ")
resposta = resposta.upper()

if resposta == "A": 
    print("Parabens voçê acertou!")
elif resposta == "B":
    print("Parabens voçê acertou!")
elif resposta == "C":
    print("Parabens voçê acertou!")
elif resposta == "D":
    print("Parabens voçê acertou!")
else:
    print("Alternativa invalida. Digite uma das alternativas mostradas na questão (A, B, C ou D).")