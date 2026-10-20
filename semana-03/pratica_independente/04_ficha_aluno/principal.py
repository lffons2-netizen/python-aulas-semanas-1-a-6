def mostrar_ficha(**dados):
    """Imprime cada informação recebida em uma linha."""
    for campo, valor in dados.items():
        print(f"{campo}: {valor}")

if __name__ == "__main__":
    nome = input("Nome: ")
    curso = input("Curso: ")
    idade = int(input("Idade: "))
    mostrar_ficha(nome=nome, curso=curso, idade=idade)
