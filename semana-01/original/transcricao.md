# Transcrição dos códigos Python

## Semana 1

Slides sem blocos ou exemplos de código Python transcritos: 1, 2, 3, 4, 5, 6, 7, 9, 11, 19, 27, 43, 44, 45, 46, 47, 48.

### Slide 8

Trecho do slide

```python
import this
```

### Slide 10

Bloco 1

```python
>>> 2 + 2
4
>>> nome = "Python"
>>> print(nome)
Python
```

Comando para sair do REPL

```python
exit()
```

### Slide 12

```python
print("Olá, mundo!")
```

### Slide 13

Os exemplos de erro de indentação foram mantidos.

Bloco 1

```python
if True:
    print("Bloco indentado")
    print("Ainda dentro do if")
print("Fora do if")
```

Bloco 2

```python
if True:
print("Erro!")
# IndentationError: faltou indentar
```

Bloco 3

```python
if True:
    print("ok")
      print("erro")
# erro: indentação inconsistente
```

### Slide 14

Bloco 1

```python
# Comentário de uma linha

"""
Comentário de várias linhas (docstring)
"""
```

Comando apresentado no texto

```python
import keyword; print(keyword.kwlist)
```

Comentário usado como exemplo no texto

```python
x = 5 # atribui 5 a x
```

### Slide 15

```python
idade = 25        # válido
_idade = 25       # válido
idade2 = 25       # válido
2idade = 25       # inválido
minha-idade = 25  # inválido
class = 25        # inválido
```

### Slide 16

```python
idade = 25
nome = "Maria"
```

### Slide 17

Bloco 1

```python
# Ruim
x = 25
d = 10.5
```

Bloco 2

```python
# Bom
idade_aluno = 25
distancia_km = 10.5
```

Bloco 3

```python
x = 10
print(x)     # 10
x = 20
print(x)     # 20
x = "agora sou texto"
print(x)     # agora sou texto
```

### Slide 18

Bloco 1

```python
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3
x = y = z = 0
print(x, y, z)  # 0 0 0
```

Bloco 2

```python
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5
```

Bloco 3

```python
PI = 3.14159
GRAVIDADE = 9.8
```

### Slide 20

Bloco 1

```python
inteiro = 42
decimal = 3.14
grande = 1_000_000
negativo = -17
cientifica = 2.5e3  # 2500.0
```

Bloco 2

```python
nome = "Python"
frase = 'Aprendendo'
texto = """várias
linhas"""
```

### Slide 21

Bloco 1

```python
ativo = True
pausado = False
print(True and False)  # False
print(5 > 3)           # True
```

Bloco 2

```python
resultado = None
print(resultado)        # None
print(type(resultado))
# <class 'NoneType'>
```

### Slide 22

Bloco 1

```python
x, y, z, w = 10, 3.14, "texto", True
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(w))  # <class 'bool'>
```

Bloco 2

```python
x = 10        # int
x = "dez"     # agora str
```

### Slide 23

Bloco 1

```python
print(5 + 2)   # 7  soma
print(5 - 2)   # 3  subtração
print(5 * 2)   # 10 multiplicação
print(5 / 2)   # 2.5 divisão
```

Bloco 2

```python
print(5 // 2)  # 2  divisão inteira
print(5 % 2)   # 1  módulo (resto)
print(5 ** 2)  # 25 potência
print(2 ** 0.5) # 1.41 raiz quadrada
```

### Slide 24

Bloco 1

```python
resultado = 2 + 3 * 4      # 14, não 20
resultado2 = (2+3) * 4     # 20
```

Bloco 2

```python
nota1, peso1 = 8.0, 2
nota2, peso2 = 6.0, 3
media = (nota1*peso1 +
  nota2*peso2) / (peso1+peso2)
print(f"Média: {media:.2f}")
```

### Slide 25

Bloco 1

```python
print(5 == 5)   # True  igual
print(5 != 3)   # True  diferente
print(5 > 3)    # True  maior
print(5 < 3)    # False menor
print(5 >= 5)   # True  maior ou igual
print(5 <= 4)   # False menor ou igual
```

Bloco 2

```python
"abc" == "abc"     # True
"abc" == "ABC"     # False (case-
sensitive)
"banana" > "abacaxi"  # True (alfabética)
```

### Slide 26

Bloco 1

```python
idade = 20
tem_carteira = True
```

Expressões apresentadas nas explicações

```python
idade >= 18 and tem_carteira
idade >= 18 or tem_carteira
not tem_carteira
```

### Slide 28

```python
def checar():
    print("função chamada")
    return True
resultado = False and checar()  # nunca imprime
```

### Slide 29

```python
x = 10
x += 5    # x = x + 5   → 15
x -= 3    # x = x - 3   → 12
x *= 2    # x = x * 2   → 24
x /= 4    # x = x / 4   → 6.0
x //= 2   # x = x // 2  → 3.0
x **= 2   # x = x ** 2  → 9.0
```

### Slide 30

A quebra de linha dentro da f-string aparece assim no PDF e foi mantida.

Bloco 1

```python
nome = "Ana"
sauda = "Olá " + nome
print(sauda)
print("Oi! " * 3)
```

Bloco 2

```python
idade = 25
nome = "Carlos"
print(f"{nome},
  {idade} anos")
```

Bloco 3

```python
preço = 19.999
f"R$ {preço:.2f}"
pct = 0.4567
f"{pct:.1%}"
```

### Slide 31

Bloco 1

```python
p = "Python"
p[0] = "J"
# TypeError!
nova = "J"+p[1:]
```

Bloco 2

```python
t = "  Top  "
t.strip()
t.upper()
t.lower()
t.replace(
  "a","b")
```

Bloco 3

```python
frase.split()
frase.count("i")
frase.find(
  "lingua")
"-".join(
  ["a","b"])
```

### Slide 32

Bloco 1

```python
nome = input("Nome? ")
print(f"Olá, {nome}!")
```

Bloco 2

```python
idade = input("Idade: ")
print(type(idade))
```

Bloco 3

```python
print("a","b","c")
# a b c
print("a","b", sep="-")
# a-b
print("x", end=" ")
print("y")  # x y
```

### Slide 33

Bloco 1

```python
t = "25"
int(t)
# str→int
float("1.75")
str(100)
bool(1)
```

Bloco 2

```python
int("abc")
# ValueError!
int("3.5")
# ValueError!
float("3.5")
# OK: 3.5
```

Bloco 3

```python
bool(0)    #False
bool(1)    #True
bool(-5)   #True
bool("")   #False
bool("oi") #True
bool(None) #False
```

### Slide 34

Bloco 1

```python
x = 10
```

Bloco 2

```python
y = x
```

Bloco 3

```python
x = 20
```

### Slide 35

Bloco 1

```python
a = "Python"
```

Bloco 2

```python
b = a
```

Bloco 3

```python
a = a + "!"
```

Chamadas apresentadas no resultado

```python
print(a)
print(b)
```

### Slide 36

Trecho do diagrama

```python
s1 = s1 + '!'
```

### Slide 37

```python
nome = "Ana"
apelido = nome
nome = "Ana Paula"
idade = 20
idade_dobrada = idade * 2
```

### Slide 38

```python
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")
```

### Slide 39

```python
valor_reais = float(input("Valor em R$: "))
cotacao_dolar = 5.10
valor_dolar = valor_reais / cotacao_dolar
print(f"R$ {valor_reais:.2f} = US$ {valor_dolar:.2f}")
```

### Slide 40

```python
celsius = float(input("Temp em °C: "))
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15
print(f"{celsius}°C = {fahrenheit:.1f}°F = {kelvin:.1f}K")
```

### Slide 41

```python
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area = largura * comprimento
perimetro = 2 * (largura + comprimento)
print(f"Área: {area:.2f} m² | Perímetro: {perimetro:.2f} m")
```

### Slide 42

```python
nome = input("Primeiro nome: ").strip().capitalize()
sobrenome = input("Sobrenome: ").strip().capitalize()
completo = f"{nome} {sobrenome}"
print(f"Nome formatado: {completo}")
print(f"Iniciais: {nome[0]}.{sobrenome[0]}.")
```
