# Ex.036- Faça um programa que: 
#  O usuario vai fornecer o tempo de vídeo do youtube e a velocidade que irá assirtir (1,25 / 1,5 /2,0).
#   O programa deve falar qual será a durabilidade do vídeo para cada tempo de aceleração.
#    Exemplo: se um video dura 1h , na velocidade 2 ele ira durar 30 min:


def duracao_do_video_acelerado(tempo_do_video):
    velocidades = [1.25, 1.5, 2.0]
    for v in velocidades:
        duracao_acelerada_do_video = tempo_do_video / v
        print (f"Na velocidade {v}x, a duração do vídeo será de {duracao_acelerada_do_video:.2f} minutos.")


tempo_do_video = float(input('Digite aqui o tempo de video do youtube que voçê irá assitir em minutos: '))
duracao_do_video_acelerado(tempo_do_video)
