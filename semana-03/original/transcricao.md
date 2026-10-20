# Transcrição dos códigos Python

## Semana 3

Slides sem blocos ou exemplos de código Python transcritos: 1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 47, 48, 49, 50, 51, 52.

### Slide 10

```python
# COM retorno
def somar(a, b):
    return a + b     # devolve o valor

# SEM retorno
def mostrar(x):
    print(x)         # devolve None

r = somar(10, 5)     # r vale 15
print(mostrar(7))    # imprime None
```

### Slide 11

```python
# retorno antecipado
def dividir(a, b):
    if b == 0:
        return None   # sai antes
    return a / b

# devolver varios valores
def dividir2(a, b):
    return a // b, a % b

q, r = dividir2(7, 2)  # 3 e 1
```

### Slide 12

```python
# procedimento: so executa acao
def saudar(nome):
    print(f"Ola, {nome}!")  # exibe
    # nao existe return aqui

saudar("Ana")        # Ola, Ana!

r = saudar("Ana")
print(r)             # None
```

### Slide 13

```python
# procedimento com parametros
def cabecalho(titulo, largura=30):
    print(titulo.center(largura))
    print("-" * largura)

cabecalho("RELATORIO")

# erro comum:
x = cabecalho("A") + 1  # TypeError
```

### Slide 14

```python
# calculadora.py  -> o modulo
PI = 3.14159

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

# nome do modulo: calculadora
```

### Slide 15

```python
# principal.py  -> usa o modulo
import calculadora as c
print(c.somar(2, 3))     # 5
print(c.PI)              # 3.14159

# importando so o que precisa
from calculadora import somar
print(somar(2, 3))       # 5
```

### Slide 16

O PDF separa def e calcular_media(notas): em duas linhas; a transcrição mantém essa apresentação.

Bloco 1

```python
def
calcular_media(notas):
    """Retorna a media."""
    t = sum(notas)
    return t / len(notas)
```

Bloco 2

```python
media = calcular_media(
    [8, 6, 10])  # GLOBAL
# print(t) -> NameError
```

Chamada apresentada na explicação

```python
help(funcao)
```

### Slide 17

```python
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
```

### Slide 18

```python
# o parametro e so um novo nome
def renomeia(lista):
    lista = [9, 9]  # novo objeto
    lista.append(1) # so o local

v = [1, 2]
renomeia(v)
print(v)            # [1, 2]

# reatribuir o parametro nunca
# altera a variavel de origem
```

### Slide 19

```python
# int, float, str e tupla: imutaveis
def dobrar(numero):
    numero = numero * 2  # novo objeto
    return numero

valor = 10
print(dobrar(valor))     # 20
print(valor)             # 10 (intacto)

# str: "abc".upper() cria outra string
```

### Slide 20

```python
# lista, dicionario e set: mutaveis
def add(lista, item):
    lista.append(item)  # altera objeto

compras = ["arroz"]
add(compras, "feijao")
print(compras)  # ['arroz', 'feijao']

# copia defensiva: protege o original
add(compras[:], "cafe")
```

### Slide 21

Bloco 1

```python
# ERRADO: lista como valor padrao
def add(item, lista=[]):
    lista.append(item)
    return lista

print(add("a"))   # ['a']
print(add("b"))   # ['a', 'b'] bug!

# o padrao e criado UMA unica vez
```

Bloco 2

```python
# CERTO: use None como padrao
def add(item, lista=None):
    if lista is None:
        lista = []      # nova a cada
    lista.append(item)
    return lista

print(add("a"))   # ['a']
print(add("b"))   # ['b'] correto
```

### Slide 22

```python
# copia defensiva antes de alterar
def total(carrinho):
    itens = carrinho[:]  # copia rasa
    itens.append("brinde")
    return itens

original = ["arroz"]
novo = total(original)
print(original)  # ['arroz']
print(novo)      # ['arroz','brinde']
```

### Slide 25

```python
# posicionais e obrigatorios
def saudar(nome, sobrenome):
    return nome + " " + sobrenome

print(saudar("Ana", "Lu"))
# Ana Lu

print(saudar("Lu", "Ana"))
# Lu Ana -> ordem trocada!
```

### Slide 26

```python
def saudar(nome, sobrenome):
    return nome + " " + sobrenome

# nomeados: a ordem fica livre
print(saudar(sobrenome="Lu",
             nome="Ana"))   # Ana Lu

# ERRADO: posicional depois
print(saudar(nome="Ana", "Lu"))
```

### Slide 27

```python
def criar(nome, ativo=True):
    if ativo:
        s = "Disponivel"
    else:
        s = "Esgotado"
    return nome + " - " + s

print(criar("Caneta"))  # Disponivel
print(criar("Caneta", False))
```

### Slide 28

```python
def somar(*numeros):
    # numeros chega como TUPLA
    return sum(numeros)

print(somar(1, 2, 3, 4))   # 10
print(somar())             # 0

valores = [1, 2, 3]
print(somar(*valores))     # 6
```

### Slide 29

```python
def perfil(**dados):
    # dados chega como DICIONARIO
    for chave, valor in dados.items():
        print(chave, ":", valor)

perfil(nome="Ana", idade=25)
# nome : Ana
# idade : 25
```

### Slide 30

```python
def rel(titulo, *itens,
        fmt="txt", **extras):
    print(titulo, fmt)
    print(itens)    # tupla
    print(extras)   # dicionario

rel("Vendas", "jan", "fev",
    fmt="pdf", autor="Ana")
```

### Slide 31

Fragmentos da tabela (assinaturas incompletas no original)

```python
def f(a, b)
f(b=2, a=1)
def f(a, b=10)
def f(*itens, **dados)
```

### Slide 32

```python
def conf(ip, /, porta, *,
         modo=True):
    print(ip, porta, modo)

conf("10.0.0.1", 8080,
     modo=False)   # OK

# conf(ip="10.0.0.1") -> erro
# conf("10.0.0.1",80,True) -> erro
```

### Slide 33

```python
def media(a, b, c):
    return (a + b + c) / 3

notas = [8, 6, 10]
print(media(*notas))   # 8.0

dados = {"a": 8, "b": 6,
         "c": 10}
print(media(**dados))  # 8.0
```

### Slide 34

```python
def dobro(x):
    return x * 2

print(dobro(5))    # 10

def dividir(a, b):
    if b == 0:
        return None   # saida antecipada
    return a / b
```

### Slide 35

```python
def dividir(a, b):
    # devolve uma TUPLA
    return a // b, a % b

q, r = dividir(17, 5)
print(q, r)    # 3 2

res = dividir(17, 5)
print(res)     # (3, 2)
```

### Slide 36

calculadora.py (pasta projeto_modulos; ao lado de script_principal.py)

```python
# calculadora.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b
```

### Slide 37

```python
# script_principal.py
import calculadora
s = calculadora.somar(2, 3)

# script_alternativo.py
from calculadora import somar
s = somar(2, 3)

import calculadora as calc
s = calc.somar(2, 3)
```

### Slide 38

```python
# Arquivo: calculadora.py

def somar(a, b):
    """Soma dois numeros."""
    return a + b

def subtrair(a, b):
    """Devolve a diferenca."""
    return a - b
```

### Slide 39

```python
# script_principal.py
import calculadora

s = calculadora.somar(10, 5)
m = calculadora.multiplicar(4, 3)

print(f"Soma: {s}")
print(f"Mult: {m}")

# Saida:  Soma: 15
#         Mult: 12
```

### Slide 40

```python
import calculadora
calculadora.somar(2, 3)

from calculadora import somar
somar(2, 3)

from calculadora import \
    subtrair as menos
print(menos(20, 8))   # 12
```

### Slide 41

```python
import calculadoraa
# ModuleNotFoundError:
# erro de digitacao no nome

# Proteja o teste do modulo:
if __name__ == "__main__":
    print(somar(2, 3))

# math.py na sua pasta
# esconde o modulo padrao
```

### Slide 42

```python
def saudar(nome):
    return "Ola, " + nome + "!"

print(saudar("Ana"))
# Ola, Ana!

msg = saudar("Edilson")
print(msg.upper())
```

### Slide 43

```python
def media(a, b, casas=2):
    m = (a + b) / 2
    return round(m, casas)

print(media(8, 6))
# 7.0

print(media(8, 5, 1))
# 6.5
```

### Slide 44

```python
def total(*precos, desc=0):
    s = sum(precos)
    return s * (1 - desc / 100)

print(total(10, 25.5, 7))
# 42.5

print(total(10, 25.5, 7, desc=10))
# 38.25
```

### Slide 45

```python
def reg(nota, boletim=None):
    """Nao altera a lista original."""
    if boletim is None:
        boletim = []
    novo = boletim[:]   # copia
    novo.append(nota)
    return novo

notas = [7]
print(reg(9, notas))  # [7, 9]
print(notas)          # [7]
```

### Slide 46

```python
# script_desafio.py
from calculadora import somar, \
                       multiplicar

def orc(qtd, preco, frete=0):
    """Total do pedido."""
    s = multiplicar(qtd, preco)
    return somar(s, frete)

print(orc(3, 49.9, 15))  # 164.7
```
