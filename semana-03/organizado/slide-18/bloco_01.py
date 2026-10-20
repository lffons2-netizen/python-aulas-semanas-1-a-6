# Semana 3 | Slide 18 | Bloco 1
# o parametro e so um novo nome
def renomeia(lista):
    lista = [9, 9]  # novo objeto
    lista.append(1) # so o local

v = [1, 2]
renomeia(v)
print(v)            # [1, 2]

# reatribuir o parametro nunca
# altera a variavel de origem
