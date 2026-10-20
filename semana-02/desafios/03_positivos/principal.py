positivos = 0
for indice in range(10):
    numero = float(input(f"Número {indice + 1}: "))
    if numero > 0:
        positivos += 1
print(f"Quantidade de positivos: {positivos}")
