def obter_data_hora_atual():
    import time
    """
    Verifica a data e a hora atual do programa.
    Utiliza da biblioteca time, para realizar a verificação
    """
    current_time = time.localtime()
    data_hora_atual = time.strftime("%d/%m/%Y %H:%M:%S", current_time)
    return data_hora_atual