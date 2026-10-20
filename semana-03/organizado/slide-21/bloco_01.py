# Semana 3 | Slide 21 | Bloco 1
# ERRADO: lista como valor padrao
def add(item, lista=[]):
    lista.append(item)
    return lista

print(add("a"))   # ['a']
print(add("b"))   # ['a', 'b'] bug!

# o padrao e criado UMA unica vez
