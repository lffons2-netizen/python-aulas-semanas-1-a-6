# Transcrição dos códigos Python

## Semana 4

Slides sem blocos ou exemplos de código Python transcritos: 1, 2, 3, 4, 5, 23, 27, 39, 40, 41, 42, 43, 44.

### Slide 6

Expressão exibida na imagem de estruturas de dados

```python
S = {1, 2, 5, 7, 9}
```

### Slide 7

Código dentro da imagem (coluna Python)

```python
frutas = ["maca", "uva", "pera"]
```

### Slide 8

```python
# declaracao da lista
lista = [10, 20, 30]
# acesso pelo indice (inicia em 0)
print(lista[0])  # imprime 10
```

### Slide 9

Exemplos da tabela, na ordem original

```python
lista.append(40)
lista.insert(1, 15)
lista.remove(20)
x = lista.pop()
lista.count(10)
lista.index(30)
lista.sort()
lista.reverse()
```

### Slide 10

```python
# lista com os precos dos produtos
precos = [10.5, 5.0, 3.2]
# soma todos os itens da lista
total = sum(precos)
# exibe o valor total da compra
print(f"Total: {total}")
```

### Slide 11

Código dentro da imagem (coluna Python)

```python
frutas = ["maca", "uva", "pera"]
```

### Slide 12

Código dentro da imagem (coluna Python)

```python
ponto = (10, 20)

print(ponto[0]) # 10
print(ponto[1]) # 20
```

### Slide 13

```python
# declaracao da tupla (parenteses)
ponto = (10, 20, 30)
# acesso pelo indice (inicia em 0)
print(ponto[0])  # imprime 10
# imprime a tupla inteira
print(ponto)      # (10, 20, 30)
# percorrendo a tupla
for valor in ponto:
    print(valor)
```

### Slide 14

Exemplos da tabela, na ordem original

```python
ponto.count(10)
ponto.index(20)
len(ponto)
max(ponto)
sum(ponto)
sorted(ponto)
tuple([1, 2, 3])
```

### Slide 15

```python
# tupla com latitude e longitude (imutavel)
local = (12.45, -32.12)
# acesso pelos indices 0 e 1
print(f"Latitude: {local[0]}, Longitude: {local[1]}")
```

### Slide 16

Código dentro da imagem (coluna Python)

```python
ponto = (10, 20)

print(ponto[0]) # 10
print(ponto[1]) # 20
```

### Slide 17

Imagem: conjunto (coluna Python)

```python
frutas = {"maca", "uva"}
```

Imagem: união (as fórmulas com ∪ são notação matemática)

```python
A = {"maca", "pera"}
B = {"uva", "pera"}
```

Imagem: interseção (as fórmulas com ∩ são notação matemática)

```python
A = {"maca", "pera"}
B = {"uva", "pera"}
```

### Slide 18

```python
# declaracao do conjunto (chaves)
frutas = {"maca", "uva", "maca"}
# duplicatas sao eliminadas
print(frutas)  # {'maca', 'uva'}
# teste de pertinencia (acesso)
print("uva" in frutas)  # True
# percorrendo o conjunto
for f in frutas:
    print(f)
```

### Slide 19

Exemplos da tabela, na ordem original

```python
frutas.add("pera")
frutas.remove("uva")
frutas.discard("kiwi")
A.union(B)
A.intersection(B)
A.difference(B)
len(frutas)
```

### Slide 20

Expressões e resultados da tabela (setas reproduzidas do slide)

```python
A = {1, 2}; B = {2, 3}  ->  A | B = {1, 2, 3}
A & B  ->  {2}
A - B  ->  {1}
A ^ B  ->  {1, 3}
```

### Slide 21

```python
# lista de entregas com nomes repetidos
entregas = ["Ana", "Joao", "Ana", "Pedro"]
# set() elimina as duplicatas
conjunto = set(entregas)
# imprime apenas os alunos unicos
print(conjunto)
```

### Slide 22

Imagem: conjunto (coluna Python)

```python
frutas = {"maca", "uva"}
```

Imagem: união (as fórmulas com ∪ são notação matemática)

```python
A = {"maca", "pera"}
B = {"uva", "pera"}
```

Imagem: interseção (as fórmulas com ∩ são notação matemática)

```python
A = {"maca", "pera"}
B = {"uva", "pera"}
```

### Slide 24

```python
# lista original de valores
lista = [10, 5, 20, 3, 42, 7]
# filtragem com list comprehension
maiores = [x for x in lista if x > 10]
print(maiores)  # [20, 42]
# mesma filtragem com filter()
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)  # [10, 20, 42]
```

### Slide 25

```python
# lista fora de ordem
lista = [10, 5, 20, 3]
# sort() ordena a propria lista
lista.sort()
print(lista)  # [3, 5, 10, 20]
# ordem decrescente
lista.sort(reverse=True)
print(lista)  # [20, 10, 5, 3]
# sorted() devolve uma nova lista
nova = sorted(lista)
```

### Slide 26

```python
# dois conjuntos de valores
A = {1, 2, 3}
B = {3, 4, 5}
# uniao: tudo de A e de B
print(A | B)  # {1, 2, 3, 4, 5}
# intersecao: o que ha nos dois
print(A & B)  # {3}
# diferenca: so o que e de A
print(A - B)  # {1, 2}
```

### Slide 28

```python
# arquivo: adicionar.py
def adicionar(estoque, produto):
    # evita duplicidade no estoque
    if produto not in estoque:
        estoque.append(produto)  # insere
    return estoque

# teste rapido do modulo
if __name__ == "__main__":
    print(adicionar(["mouse"], "teclado"))
```

### Slide 29

```python
# arquivo: remover.py
def remover(estoque, produto):
    # so remove se o item existir
    if produto in estoque:
        estoque.remove(produto)
    else:
        print("Produto nao encontrado")
    return estoque

if __name__ == "__main__":
    print(remover(["mouse", "hd"], "hd"))
```

### Slide 30

```python
# arquivo: atualizar.py
def atualizar(estoque, antigo, novo):
    # localiza o indice do produto
    if antigo in estoque:
        i = estoque.index(antigo)
        estoque[i] = novo  # substitui
    return estoque

if __name__ == "__main__":
    print(atualizar(["mose"], "mose",
                    "mouse"))
```

### Slide 31

```python
# arquivo: iterar.py
def iterar(estoque):
    # enumerate da indice e valor
    for i, produto in enumerate(estoque,
                                 start=1):
        print(i, "-", produto)
    print("Total:", len(estoque))

if __name__ == "__main__":
    iterar(["mouse", "teclado"])
```

### Slide 32

```python
# arquivo: pertencimento.py
def existe(estoque, produto):
    # o operador in devolve True/False
    return produto in estoque

if __name__ == "__main__":
    lista = ["mouse", "teclado"]
    if existe(lista, "mouse"):
        print("Ja cadastrado")
    else:
        print("Pode comprar")
```

### Slide 33

```python
# arquivo: principal.py
from adicionar import adicionar
from remover import remover
from atualizar import atualizar
from iterar import iterar
from pertencimento import existe
estoque = ["mouse", "mose", "hd"]
adicionar(estoque, "teclado")
atualizar(estoque, "mose", "mouse2")
remover(estoque, "hd")
if existe(estoque, "teclado"):
    iterar(estoque)  # relatorio final
```

### Slide 34

```python
# Exercicio 1: criar lista de numeros
numeros = []  # lista vazia
qtd = int(input("Quantos numeros? "))
for i in range(qtd):
    n = int(input("Digite um numero: "))
    numeros.append(n)  # insere no fim
print("Lista:", numeros)
print("Tamanho:", len(numeros))
```

### Slide 35

```python
# Exercicio 2: filtrar numeros pares
texto = input("Numeros separados por espaco: ")
numeros = [int(x) for x in texto.split()]
# filtra os divisiveis por 2
pares = [n for n in numeros if n % 2 == 0]
print("Digitados:", numeros)
print("Pares:", pares)
```

### Slide 36

```python
# Exercicio 3: ordenar a lista
texto = input("Numeros separados por espaco: ")
numeros = [int(x) for x in texto.split()]
numeros.sort()  # ordem crescente
print("Crescente:", numeros)
# copia ordenada ao contrario
print("Decrescente:", sorted(numeros,
                              reverse=True))
```

### Slide 37

```python
# Exercicio 4: conjunto sem duplicatas
texto = input("Palavras separadas por espaco: ")
palavras = texto.split()
# set() elimina os repetidos
unicos = set(palavras)
print("Digitadas:", len(palavras))
print("Unicas:", len(unicos))
print(sorted(unicos))
```

### Slide 38

```python
# Exercicio 5: tupla de estatisticas
texto = input("Notas separadas por espaco: ")
notas = [float(x) for x in texto.split()]
# tupla e imutavel: protege o resultado
estat = (min(notas), max(notas),
         sum(notas) / len(notas))
print("Minimo:", estat[0])
print("Maximo:", estat[1])
print("Media: %.2f" % estat[2])
```
