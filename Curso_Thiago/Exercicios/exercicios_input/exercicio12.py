# 12- Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos:

dias = int(input("Digite aqui os dias: "))
horas = int(input("Digite agora as horas: "))
minutos = int(input("Digite agora os minutos: "))
segundos = int(input("Digite agora os segundos: "))

dias_convertidos_em_segundos = dias * 24 * 60 * 60
horas_convertidos_em_segundos = horas * 60 * 60
minutos_convertidos_em_segundos = minutos * 60

soma_total_em_segundos = dias_convertidos_em_segundos + horas_convertidos_em_segundos + minutos_convertidos_em_segundos + segundos

print(f"De acordo com o dia, hora, minutos e segundos digitados, a soma do total convertido em segundos será: {soma_total_em_segundos} segundos")