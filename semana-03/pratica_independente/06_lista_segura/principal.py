def adicionar_seguro(lista, item):
    """Retorna uma cópia com o novo item, sem alterar a lista recebida."""
    nova_lista = lista[:]
    nova_lista.append(item)
    return nova_lista

if __name__ == "__main__":
    original = input("Itens separados por vírgula: ").split(",")
    item = input("Novo item: ")
    nova = adicionar_seguro(original, item)
    print(f"Original: {original}")
    print(f"Nova: {nova}")
