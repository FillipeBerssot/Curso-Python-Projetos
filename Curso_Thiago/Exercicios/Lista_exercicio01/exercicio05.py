# Ex.05- Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
# que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

pais_a = 80000
crescimento_pais_a = 0.03

pais_b = 200000
crescimento_pais_b = 0.015

anos_necessarios = 0

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a * crescimento_pais_a)
    pais_b = pais_b + (pais_b * crescimento_pais_b)
    anos_necessarios = anos_necessarios + 1

print(f'O país A precisará de {anos_necessarios} anos de crescimento para poder ultrapassar ou se igualar ao país B.')
print(f'O país A em {anos_necessarios} anos, terá {pais_a:.0f} habitantes.')
print(f'O país B em {anos_necessarios} anos, terá {pais_b:.0f} habitantes.')

