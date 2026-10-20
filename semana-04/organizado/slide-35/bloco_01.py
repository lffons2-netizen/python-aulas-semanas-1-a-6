# Semana 4 | Slide 35 | Bloco 1
# Exercicio 2: filtrar numeros pares
texto = input("Numeros separados por espaco: ")
numeros = [int(x) for x in texto.split()]
# filtra os divisiveis por 2
pares = [n for n in numeros if n % 2 == 0]
print("Digitados:", numeros)
print("Pares:", pares)
