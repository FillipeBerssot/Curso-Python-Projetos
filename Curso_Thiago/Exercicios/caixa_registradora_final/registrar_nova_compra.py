def registrar_nova_compra():
    """
    Verifica se o usuario deseja registrar uma nova compra,
    caso NÃO ele encerra o programa
    caso SIM ele reinicia o programa.
    """
    while True:
        nova_compra_usuario = input("\nDeseja registrar uma nova compra? (s/n): ").strip().lower()
        if nova_compra_usuario == 's':
            return 's'  
        elif nova_compra_usuario == 'n':
            return 'n' 
        else:
            print("Opção inválida. Por favor, digite 's' para continuar ou 'n' para sair.")
