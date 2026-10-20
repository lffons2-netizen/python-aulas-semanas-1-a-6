nomes = []
categorias = {"Aluno": 0, "Professor": 0, "Funcionário": 0}
while True:
    comando = input("Enter para cadastrar ou sair: ").strip().lower()
    if comando == "sair":
        break
    quantidade = int(input("Quantos cadastros neste lote? "))
    for indice in range(quantidade):
        nome = input(f"Nome {indice + 1}: ").strip()
        idade = int(input("Idade: "))
        if idade < 18:
            print("Cadastro recusado: idade mínima de 18 anos.")
            continue
        elif not nome:
            print("Cadastro recusado: nome vazio.")
            continue
        else:
            opcao = int(input("1-Aluno | 2-Professor | 3-Funcionário: "))
        match opcao:
            case 1:
                categoria = "Aluno"
            case 2:
                categoria = "Professor"
            case 3:
                categoria = "Funcionário"
            case _:
                print("Categoria inválida.")
                continue
        nomes.append(nome)
        categorias[categoria] += 1
print(f"Total de cadastros: {len(nomes)}")
for categoria, quantidade in categorias.items():
    print(f"{categoria}: {quantidade}")
print(f"Nomes: {nomes}")
