from collections import Counter

def media(valores):
    """Calcula a média; rejeita uma coleção vazia."""
    if not valores:
        raise ValueError("Informe pelo menos um valor.")
    return sum(valores) / len(valores)

def mediana(valores):
    """Calcula a mediana de uma coleção não vazia."""
    if not valores:
        raise ValueError("Informe pelo menos um valor.")
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    if len(ordenados) % 2:
        return ordenados[meio]
    return (ordenados[meio - 1] + ordenados[meio]) / 2

def moda(valores):
    """Retorna todas as modas em empate, na ordem da primeira ocorrência."""
    if not valores:
        raise ValueError("Informe pelo menos um valor.")
    contagens = Counter(valores)
    maior = max(contagens.values())
    return [valor for valor, frequencia in contagens.items() if frequencia == maior]
