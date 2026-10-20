# Organização: contexto/continuação reunido para execução.
print("=== MENU DE INSCRIÇÃO DA MARATONA ===")
print("1 - Maratona Completa")
print("2 - Meia Maratona")
print("3 - Corrida de Estreia")

opcao = int(input("Escolha o número da sua categoria: "))

print("\n--- Resultado ---")

match opcao:
    case 1:
        print("Inscrição Confirmada: Maratona
Completa (42.195 km)") case 2: print("Inscrição Confirmada: Meia Maratona
(21.097 km)") case 3: print("Inscrição Confirmada: Corrida de
Estreia (5 km)")
    case _:
        # O sublinhado (_) substitui o "caso contrario" do Portugol
        print("Erro: Categoria inexistente! Escolha
de 1 a 3.")
