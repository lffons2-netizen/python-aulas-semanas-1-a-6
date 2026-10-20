import estatistica as est
valores = [float(valor) for valor in input("Valores separados por espaço: ").split()]
try:
    print(f"Média: {est.media(valores):.2f}")
    print(f"Mediana: {est.mediana(valores):.2f}")
    print(f"Moda(s): {est.moda(valores)}")
except ValueError as erro:
    print(f"Erro: {erro}")
