# Ex.019 - Faça um programa para verificar se um aluno foi aprovado. Faça a média das notas dele, se for superior
# a 7 ele esta aprovado:

# notas = [8, 7, 6, 5]

def verificar_aluno_aprovado(notas):
    media = sum(notas) / len(notas) 

    if media > 7:
        return f'A média do aluno é {media} e ele está acima da média. ALUNO APROVADO!'
    else:
        return f'A média do aluno é {media} e ele não está acima da média. ALUNO REPROVADO!'


notas = [8, 7, 6, 5]
print(verificar_aluno_aprovado(notas))

notas2 = [8, 7.5, 6.5, 7]
print(verificar_aluno_aprovado(notas2))