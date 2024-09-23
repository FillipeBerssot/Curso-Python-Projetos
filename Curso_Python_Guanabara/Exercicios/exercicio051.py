# Ex.051- Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmetica (PA).
# No final, mostre os 10 primeiros termos dessa progressão:

print('=' * 30)
print('TERMOS DE UMA PA')
print('=' * 30)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end='-> ' )
print('ACABOU')