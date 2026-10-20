quantidade = 0
nome = input("Nome (fim para encerrar): ").strip()
while nome.lower() != "fim":
    if nome:
        quantidade += 1
    nome = input("Nome (fim para encerrar): ").strip()
print(f"Nomes digitados: {quantidade}")
