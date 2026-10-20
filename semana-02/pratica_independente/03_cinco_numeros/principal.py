numeros = []
for indice in range(5):
    numeros.append(float(input(f"Número {indice + 1}: ")))
print(f"Soma: {sum(numeros):.2f}")
print(f"Média: {sum(numeros) / len(numeros):.2f}")
print(f"Maior: {max(numeros)}")
print(f"Menor: {min(numeros)}")
