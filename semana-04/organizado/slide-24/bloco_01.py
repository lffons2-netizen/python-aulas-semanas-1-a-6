# Semana 4 | Slide 24 | Bloco 1
# lista original de valores
lista = [10, 5, 20, 3, 42, 7]
# filtragem com list comprehension
maiores = [x for x in lista if x > 10]
print(maiores)  # [20, 42]
# mesma filtragem com filter()
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)  # [10, 20, 42]
