# Organização: contexto/continuação reunido para execução.
opcao = int(input("Escolha (1-2): "))
match opcao:
    case 1:
        print("Iniciar")
    case 2:
        print("Configurações")
    case _:
        print("Opção inválida")
