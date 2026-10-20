def calcular_caixa(*precos):
    """Retorna total, maior preço e média; sem itens, retorna três zeros."""
    if not precos:
        return 0.0, 0.0, 0.0
    return sum(precos), max(precos), sum(precos) / len(precos)

if __name__ == "__main__":
    precos = [float(valor) for valor in input("Preços separados por espaço: ").split()]
    total, maior, media = calcular_caixa(*precos)
    print(f"Total: {total:.2f} | Mais caro: {maior:.2f} | Média: {media:.2f}")
