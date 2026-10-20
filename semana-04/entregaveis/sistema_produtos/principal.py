def analisar_produtos(produtos, limite, modo="acima"):
    """Filtra preços, ordena e retorna categorias e tupla de estatísticas."""
    if modo not in ("acima", "abaixo"):
        raise ValueError("Modo deve ser acima ou abaixo.")
    if modo == "acima":
        filtrados = [p for p in produtos if p["preco"] > limite]
    else:
        filtrados = [p for p in produtos if p["preco"] < limite]
    crescente = sorted(produtos, key=lambda p: p["preco"])
    decrescente = sorted(produtos, key=lambda p: p["preco"], reverse=True)
    categorias = set(p["categoria"] for p in produtos)
    precos = [p["preco"] for p in produtos]
    estatisticas = (min(precos), max(precos), sum(precos) / len(precos)) if precos else ()
    return filtrados, crescente, decrescente, categorias, estatisticas

def mostrar_produtos(titulo, produtos):
    """Exibe uma lista de produtos com nome, preço e categoria."""
    print(f"\n{titulo}")
    for produto in produtos:
        print(f"{produto['nome']} | R$ {produto['preco']:.2f} | {produto['categoria']}")

def main():
    """Cadastra produtos e apresenta o relatório solicitado."""
    produtos = []
    quantidade = int(input("Quantidade de produtos: "))
    for indice in range(quantidade):
        nome = input(f"Nome do produto {indice + 1}: ").strip()
        preco = float(input("Preço: "))
        categoria = input("Categoria: ").strip()
        if preco < 0 or not nome or not categoria:
            raise ValueError("Informe nome, categoria e preço não negativo.")
        produtos.append({"nome": nome, "preco": preco, "categoria": categoria})
    limite = float(input("Preço limite: "))
    modo = input("Filtrar acima ou abaixo: ").strip().lower()
    filtrados, crescente, decrescente, categorias, estatisticas = analisar_produtos(produtos, limite, modo)
    mostrar_produtos("Filtrados", filtrados)
    mostrar_produtos("Ordem crescente", crescente)
    mostrar_produtos("Ordem decrescente", decrescente)
    print(f"Categorias únicas: {sorted(categorias)}")
    if estatisticas:
        menor, maior, media = estatisticas
        print(f"Menor: {menor:.2f} | Maior: {maior:.2f} | Média: {media:.2f}")
    else:
        print("Nenhum produto cadastrado; estatísticas: ().")

if __name__ == "__main__":
    try:
        main()
    except ValueError as erro:
        print(f"Erro: {erro}")
