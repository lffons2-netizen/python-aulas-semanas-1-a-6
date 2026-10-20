# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 34

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
