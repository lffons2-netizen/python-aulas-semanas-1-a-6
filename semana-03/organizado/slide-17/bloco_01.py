# Semana 3 | Slide 17 | Bloco 1
# imutaveis: int, float, str, tupla
def muda(x):
    x = 10        # so o nome local
n = 5
muda(n)
print(n)          # 5 -> nao mudou

# mutaveis: lista, dicionario, set
def inclui(lst):
    lst.append(4) # altera o objeto
v = [1, 2, 3]; inclui(v)
print(v)          # [1, 2, 3, 4]
