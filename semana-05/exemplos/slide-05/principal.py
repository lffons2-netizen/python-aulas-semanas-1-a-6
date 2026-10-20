# Semana 5 | Slide 5 | Bloco 1
# Lista de produtos (mutável, ordenada)
produtos = [
    ("Mouse", 45.90, "Periféricos"),
    ("Teclado", 120.00, "Periféricos"),
    ("Monitor", 899.00, "Vídeo"),
    ("Mouse", 45.90, "Periféricos"),  # duplicata
]

# Conjunto de categorias únicas (sem duplicatas)
categorias = set(p[2] for p in produtos)
print(categorias)  # {'Periféricos', 'Vídeo'}

# Ordenação por preço (crescente)
produtos_ordenados = sorted(produtos, key=lambda p: p[1])
print(produtos_ordenados)

# Tupla de estatísticas (imutável)
menor = min(produtos, key=lambda p: p[1])[1]
maior = max(produtos, key=lambda p: p[1])[1]
media = sum(p[1] for p in produtos) / len(produtos)
estatisticas = (menor, maior, round(media, 2))
print(estatisticas)  # (45.9, 899.0, 277.7)
