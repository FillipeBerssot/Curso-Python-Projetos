# Ex.06- Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.(4 e 5):
# Solução: Validação de dados em Python

pais_a = float(input('Informe aqui a quantidade de habitantes no país A: '))
crescimento_pais_a = float(
    input('Informe agora a porcentagem da taxa de crescimento do país A: ')
)

pais_b = float(input('Informe aqui a quantidade de habitantes no país B: '))
crescimento_pais_b = float(
    input('Informe agora a porcentagem da taxa de crescimento do país B: ')
)

anos_necessarios = 0

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a * (crescimento_pais_a / 100))
    pais_b = pais_b + (pais_b * (crescimento_pais_b / 100))
    anos_necessarios = anos_necessarios + 1

print(
    f'O país A precisará de {anos_necessarios} anos de crescimento para poder ultrapassar ou se igualar ao país B.'
)
print(f'O país A em {anos_necessarios} anos, terá {pais_a:.0f} habitantes.')
print(f'O país B em {anos_necessarios} anos, terá {pais_b:.0f} habitantes.')
