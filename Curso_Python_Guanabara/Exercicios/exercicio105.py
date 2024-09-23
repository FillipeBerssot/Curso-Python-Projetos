# Ex. 105- Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionario
# com as seguintes informações:
# - Quantidade de notas:
# - A maior nota:
# - A menor nota:
# - A medida da turma:
# - situação (+ 7 boa, - 7 razoavel, - 6 ruim)

def notas(* valores, show=False):
    quantidade_notas = len(valores)
    maior_nota = max(valores)
    menor_nota = min(valores)
    media = sum(valores) / len(valores)

    resultado ={
        'Quantidade de notas': quantidade_notas,
        'As Notas': valores,
        'Maior Nota': maior_nota,
        'Menor Nota': menor_nota,
        'Média': media,
    }

    if show:
        if media >= 7:
            resultado['Situação'] = 'BOA'
        elif media >= 5:
            resultado['Situação'] = 'RAZOÁVEL'
        else:
            resultado['Situação'] = 'RUIM'

    return resultado


resp = notas(4.5, 10, 6.5)
resp2 = notas(6.5, 7.5, 8.5, 10, 5.5, show=True)
print(resp)
print(resp2)