# Transcrição dos códigos Python

## Semana 2

Slides sem blocos ou exemplos de código Python transcritos: 1, 2, 3, 4, 5, 6, 7, 10, 12, 13, 16, 17, 19, 23, 24, 25, 26, 35, 37, 38, 39, 42, 43, 45, 50, 51, 52, 53, 54, 55.

### Slide 8

```python
#simples
if condicao:    # código se for verdade

#composta
if condicao:
    # código se for verdade
else:
    # código se for falso
```

### Slide 9

```python
#encadeado
if condicao1:
    # código se condicao1 for verdade
elif condicao2:
    # código se condicao2 for verdade
else:
    # código se nenhuma for verdade
```

### Slide 11

```python
if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")
```

### Slide 14

```python
# Entrada de dados (com conversão para número real)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
```

### Slide 15

```python
# Processamento (Cálculo da média)
media = (nota1 + nota2 + nota3) / 3

# Exibição da média formatada com duas casas decimais
print(f"Média: {media:.2f}")

# Estrutura Condicional
if media >= 7.0:
    print("Classificação: APROVADO")
elif media >= 5.0:
    print("Classificação: RECUPERAÇÃO")
else:
    print("Classificação: REPROVADO")
```

### Slide 18

```python
match opcao:
    case 1:
        print("Iniciar")
    case 2:
        print("Configurações")
    case _:
        print("Opção inválida")
```

### Slide 20

```python
print("=== MENU DE INSCRIÇÃO DA MARATONA ===")
print("1 - Maratona Completa")
print("2 - Meia Maratona")
print("3 - Corrida de Estreia")

opcao = int(input("Escolha o número da sua
categoria: "))

print("\n--- Resultado ---")
```

### Slide 21

```python
match opcao:
    case 1:
        print("Inscrição Confirmada: Maratona
Completa (42.195 km)")
    case 2:
        print("Inscrição Confirmada: Meia Maratona
(21.097 km)")
    case 3:
        print("Inscrição Confirmada: Corrida de
Estreia (5 km)")
```

### Slide 22

Continuação do match do slide 21; a indentação inicial foi mantida.

```python
    case _:
        # O sublinhado (_) substitui o "caso
contrario" do Portugol
        print("Erro: Categoria inexistente! Escolha
de 1 a 3.")
```

### Slide 27

```python
for variavel_item in sequencia:
    # Código que vai ser repetido
(obrigatoriamente indentado)
```

### Slide 28

```python
for i in range(1, 11):
    print(i)
```

### Slide 29

```python
cores = ["azul", "verde", "vermelho"]
for cor in cores:
    print(cor)   # Imprime cada cor
diretamente, sem precisar de contadores
```

### Slide 30

```python
for letra in "Python":
    print(letra)
```

### Slide 31

Chamadas apresentadas no slide

```python
range(1, 10)
range(10)
```

### Slide 32

```python
for i in range(0, 20, 2):
    print(i)
```

### Slide 33

```python
for i in range(10, 0, -1):
    print(i)
```

### Slide 34

Chamada apresentada na explicação

```python
range(5)
```

### Slide 36

```python
soma = 0
# Começa em 2, vai até 101 (para incluir o 100) e
pula de 2 em 2
for i in range(2, 101, 2):
    soma += i  # O mesmo que: soma = soma + i

print(f"A soma dos números pares de 1 a 100 é:
{soma}")
```

### Slide 40

```python
while condicao_logica:
    # Código que vai ser repetido
(obrigatoriamente indentado)
    # IMPORTANTE: Mudar algo aqui dentro
para a condição se tornar falsa!
```

### Slide 41

```python
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
```

### Slide 44

```python
# Primeira tentativa de leitura
nota = float(input("Digite uma nota entre 0 e 10: "))

# O loop roda ENQUANTO a nota for INVÁLIDA
while nota < 0.0 or nota > 10.0:
    print("Erro! Nota inválida.")
    nota = float(input("Digite novamente uma nota entre 0
e 10: "))

# Se saiu do loop, é porque a nota é válida
print(f"\nNota gravada com sucesso: {nota}")
```

### Slide 46

```python
nota = float(input("Digite a nota: "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

### Slide 47

```python
opcao = int(input("Escolha (1-3): "))

match opcao:
    case 1:
        print("Somando...")
    case 2:
        print("Subtraindo...")
    case 3:
        print("Multiplicando...")
    case _:
        print("Opção inválida")
```

### Slide 48

```python
for i in range(1, 11):
    print(i)
```

### Slide 49

```python
n = int(input("Digite um número (0 para sair): "))

while n != 0:
    print(f"Você digitou: {n}")
    n = int(input("Digite outro número: "))
```
