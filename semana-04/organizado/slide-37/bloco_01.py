# Semana 4 | Slide 37 | Bloco 1
# Exercicio 4: conjunto sem duplicatas
texto = input("Palavras separadas por espaco: ")
palavras = texto.split()
# set() elimina os repetidos
unicos = set(palavras)
print("Digitadas:", len(palavras))
print("Unicas:", len(unicos))
print(sorted(unicos))
