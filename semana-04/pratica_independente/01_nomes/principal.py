nomes = []
quantidade = int(input("Quantos nomes deseja digitar? "))
for indice in range(quantidade):
    nomes.append(input(f"Nome {indice + 1}: ").strip())
unicos = set(nomes)
ordenados = sorted(unicos)
extremos = (ordenados[0], ordenados[-1]) if ordenados else ()
print(f"Nomes digitados: {len(nomes)}")
print(f"Nomes únicos: {len(unicos)}")
print(f"Lista ordenada: {ordenados}")
print(f"Primeiro e último: {extremos}")
