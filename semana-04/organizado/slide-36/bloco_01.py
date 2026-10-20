# Semana 4 | Slide 36 | Bloco 1
# Exercicio 3: ordenar a lista
texto = input("Numeros separados por espaco: ")
numeros = [int(x) for x in texto.split()]
numeros.sort()  # ordem crescente
print("Crescente:", numeros)
# copia ordenada ao contrario
print("Decrescente:", sorted(numeros,
                              reverse=True))
