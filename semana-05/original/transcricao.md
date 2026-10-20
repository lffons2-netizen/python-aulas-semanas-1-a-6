# Transcrição dos códigos Python

## Semana 5

Slides sem blocos ou exemplos de código Python transcritos: 2, 3, 4, 29, 30, 32, 33, 34.

### Slide 1

aula05.py

```python
import re

try:
    with open("contatos.txt") as f:
        texto = f.read()
    emails = re.findall(r"\S+@\S+", texto)
    print(emails)
except FileNotFoundError:
    print("Arquivo não encontrado!")
```

### Slide 5

recap_semana4.py

```python
# Lista de produtos (mutável, ordenada)
produtos = [
    ("Mouse", 45.90, "Periféricos"),
    ("Teclado", 120.00, "Periféricos"),
    ("Monitor", 899.00, "Vídeo"),
    ("Mouse", 45.90, "Periféricos"),  # duplicata
]

# Conjunto de categorias únicas (sem duplicatas)
categorias = set(p[2] for p in produtos)
print(categorias)  # {'Periféricos', 'Vídeo'}

# Ordenação por preço (crescente)
produtos_ordenados = sorted(produtos, key=lambda p: p[1])
print(produtos_ordenados)

# Tupla de estatísticas (imutável)
menor = min(produtos, key=lambda p: p[1])[1]
maior = max(produtos, key=lambda p: p[1])[1]
media = sum(p[1] for p in produtos) / len(produtos)
estatisticas = (menor, maior, round(media, 2))
print(estatisticas)  # (45.9, 899.0, 277.7)
```

### Slide 6

conjuntos.py

```python
A = {1, 2, 3}
B = {3, 4, 5}

# União
print(A | B)          # {1, 2, 3, 4, 5}

# Interseção
print(A & B)          # {3}

# Diferença
print(A - B)          # {1, 2}

# Diferença simétrica
print(A ^ B)          # {1, 2, 4, 5}
```

### Slide 7

filtragem.py

```python
# Lista original
numeros = [10, 5, 20, 3, 42, 7]

# Filtragem com list comprehension
maiores = [x for x in numeros if x > 10]
print(maiores)  # [20, 42]

# Filtragem com filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [10, 20, 42]

# Ordenação
numeros.sort()
print(numeros)  # [3, 5, 7, 10, 20, 42]

# Ordem decrescente
numeros.sort(reverse=True)
print(numeros)  # [42, 20, 10, 7, 5, 3]
```

### Slide 8

adicionar.py

```python
def adicionar(estoque, produto):
    if produto not in estoque:
        estoque.append(produto)
    return estoque
```

remover.py

```python
def remover(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
    else:
        print("Produto não encontrado")
    return estoque
```

principal.py

```python
from adicionar import adicionar
from remover import remover

estoque = ["mouse", "teclado"]
adicionar(estoque, "monitor")
remover(estoque, "mouse")
print(estoque)  # ['teclado', 'monitor']
```

### Slide 9

estatisticas.py

```python
# Notas de alunos
notas = [7.5, 9.0, 6.0, 8.5, 10.0]

# Tupla de estatísticas (imutável)
estatisticas = (min(notas), max(notas), sum(notas) / len(notas))
print(f"Mínimo: {estatisticas[0]}")
print(f"Máximo: {estatisticas[1]}")
print(f"Média: {estatisticas[2]:.2f}")
```

### Slide 10

O original contém with print(conteudo) open(...). Esse erro foi mantido, sem correção.

sintaxe.py

```python
arquivo = open("nome.txt", "modo", encoding="utf-8")
```

leitura.py

```python
# Abrindo para leitura
with print(conteudo) open("dados.txt", "r",
encoding="utf-8") as f:
    conteudo = f.read()
```

### Slide 11

leitura_metodos.py

```python
# read() — lê tudo
with open("dados.txt", "r", encoding="utf-8") as f:
    print(f.read())

# readline() — lê uma linha
with open("dados.txt", "r", encoding="utf-8") as f:
    print(f.readline())  # primeira linha
    print(f.readline())  # segunda linha

# readlines() — lista de linhas
with open("dados.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()
    print(linhas)  # ['linha1\n', 'linha2\n', ...]

# Iteração direta (mais eficiente)
with open("dados.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())
```

### Slide 12

escrita.py

```python
# Escrita (sobrescreve)
with open("saida.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha\n")
    f.write("Segunda linha\n")

# Append (adiciona ao final)
with open("saida.txt", "a", encoding="utf-8") as f:
    f.write("Terceira linha\n")

# writelines
linhas = ["Linha A\n", "Linha B\n", "Linha C\n"]
with open("saida.txt", "w", encoding="utf-8") as f:
    f.writelines(linhas)
```

### Slide 13

Bloco 1

```python
f = open("dados.txt", "r")
try:
    conteudo = f.read()
finally:
    f.close()
```

Bloco 2

```python
with open("dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
# arquivo fechado automaticamente
```

### Slide 14

csv_exemplo.py

```python
import csv

# Leitura
with open("dados.csv", "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)

# Escrita
with open("saida.csv", "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["Ana", 25])
    escritor.writerow(["Bruno", 30])
```

json_exemplo.py

```python
import json

# Leitura
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
    print(dados)

# Escrita
dados = {"nome": "Ana", "idade": 25}
with open("saida.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)
```

### Slide 15

Sintaxes da tabela

```python
re.match(padrao, texto)
re.search(padrao, texto)
re.findall(padrao, texto)
re.sub(padrao, novo, texto)
re.split(padrao, texto)
```

exemplo_basico.py

```python
import re

texto = "Meu email é ana@email.com e o dela é bruno@email.com"
padrao = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(padrao, texto)
print(emails)  # ['ana@email.com', 'bruno@email.com']
```

### Slide 16

metacaracteres.py

```python
import re

# Validar data no formato YYYY-MM-DD
padrao = r"^\d{4}-\d{2}-\d{2}$"
print(re.match(padrao, "2026-08-30"))  # match
print(re.match(padrao, "30/08/2026"))  # None

# Extrair números de um texto
texto = "Comprei 3 livros por 120 reais"
numeros = re.findall(r"\d+", texto)
print(numeros)  # ['3', '120']
```

### Slide 17

funcoes_re.py

```python
import re

texto = "O ano de 2026 começou e 2027 virá."

# match — verifica o início
print(re.match(r"O ano", texto))  # match

# search — procura em qualquer lugar
print(re.search(r"\d{4}", texto))  # 2026

# findall — todas as ocorrências
print(re.findall(r"\d{4}", texto))  # ['2026', '2027']

# sub — substituição
novo = re.sub(r"\d{4}", "ANO", texto)
print(novo)  # "O ano de ANO começou e ANO virá."

# split — divisão
partes = re.split(r"\s+", texto)
print(partes)  # ['O', 'ano', 'de', '2026', ...]
```

### Slide 18

validacoes.py

```python
import re

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))

def validar_telefone(telefone):
    padrao = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    return bool(re.match(padrao, telefone))

def validar_data(data):
    padrao = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(padrao, data))

# Testes
print(validar_email("ana@email.com"))       # True
print(validar_cpf("123.456.789-00"))        # True
print(validar_telefone("(11) 91234-5678"))  # True
print(validar_data("2026-08-30"))           # True
```

### Slide 19

extrair_ips.py

```python
import re


log = """
2026-08-30 10:00:00 192.168.1.1 GET /index.html
2026-08-30 10:05:00 10.0.0.5 POST /login
2026-08-30 10:10:00 192.168.1.1 GET /dashboard
"""

padrao_ip = r"\d{1,3}(?:\.\d{1,3}){3}"
ips = re.findall(padrao_ip, log)
print(ips)  # ['192.168.1.1', '10.0.0.5', '192.168.1.1']

# IPs únicos
print(set(ips))  # {'192.168.1.1', '10.0.0.5'}
```

mascarar_cpf.py

```python
texto = "CPF: 123.456.789-00, outro: 987.654.321-00"
mascarado = re.sub(r"\d{3}\.\d{3}\.\d{3}-\d{2}", "***.***.***-**", texto)
print(mascarado)  # "CPF: ***.***.***-**, outro: ***.***.***-**"
```

### Slide 20

excecoes.py

```python
try:
    # código que pode falhar
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Valor inválido!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")
else:
    print("Resultado:", resultado)
finally:
    print("Fim da execução.")
```

### Slide 21

arquivo_seguro.py

```python
try:
    with open("nao_existe.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
except PermissionError:
    print("Sem permissão para ler o arquivo!")
```

### Slide 22

raise.py

```python
def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor

try:
    sacar(100, 200)
except ValueError as e:
    print(f"Erro: {e}")  # Erro: Saldo insuficiente
```

excecao_personalizada.py

```python
class SaldoInsuficienteError(Exception):
    """Exceção para saldo insuficiente."""
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(
            f"Saldo {saldo} insuficiente "
            f"para saque de {valor}")
    return saldo - valor

try:
    sacar(100, 200)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
```

### Slide 23

Os dois painéis são partes do mesmo código; a indentação da continuação foi mantida.

analise_log.py — início

```python
import re

def analisar_log(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
        return
    except PermissionError:
        print(f"Sem permissão para ler {caminho}.")
        return
```

analise_log.py — continuação

```python
    else:
        padrao_ip = r"\d{1,3}(?:\.\d{1,3}){3}"
        padrao_data = r"\d{4}-\d{2}-\d{2}"
        ips = []
        datas = []
        for linha in linhas:
            ips.extend(re.findall(padrao_ip, linha))
            datas.extend(re.findall(padrao_data, linha))

        print(f"Total de linhas: {len(linhas)}")
        print(f"IPs únicos: {len(set(ips))}")
        print(f"Datas encontradas: {len(set(datas))}")
        print(f"IPs: {set(ips)}")
    finally:
        print("Análise concluída.")

# Executar
analisar_log("acesso.log")
```

### Slide 24

contador_palavras.py

```python
def contar_palavras(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    palavras = conteudo.split()
    print(f"Total de palavras: {len(palavras)}")
    print(f"Palavras únicas: {len(set(palavras))}")

contar_palavras("texto.txt")
```

### Slide 25

validador_cadastro.py

```python
import re

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))

# Testes
emails = ["ana@email.com", "invalido", "bruno@empresa.com.br"]
for e in emails:
    print(f"{e}: {'válido' if validar_email(e) else 'inválido'}")

cpfs = ["123.456.789-00", "12345678900"]
for c in cpfs:
    print(f"{c}: {'válido' if validar_cpf(c) else 'inválido'}")
```

### Slide 26

divisao_segura.py

```python
def dividir():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = a / b
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    else:
        print(f"Resultado: {resultado:.2f}")
    finally:
        print("Operação encerrada.")

dividir()
```

### Slide 27

filtrar_produtos.py

```python
import csv

def filtrar_produtos(caminho, preco_min):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                preco = float(linha["preco"])
                if preco >= preco_min:
                    print(f"{linha['nome']}: R$ {preco:.2f}")
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except KeyError:
        print("Coluna 'preco' não encontrada no CSV.")
    except ValueError:
        print("Valor de preço inválido.")

filtrar_produtos("produtos.csv", 100)
```

### Slide 28

validar_idade.py

```python
class IdadeInvalidaError(Exception):
    """Exceção para idade menor que 18."""
    pass

def validar_idade(idade):
    if idade < 18:
        raise IdadeInvalidaError(f"Idade {idade} é menor que 18.")
    return True

try:
    validar_idade(15)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
else:
    print("Idade válida.")
```

### Slide 31

Validador do gabarito (quebra de linha mantida como exibida)

```python
re.match(r"^[\w\.-]+@[\w\.-
]+\.\w+$", email)
```
