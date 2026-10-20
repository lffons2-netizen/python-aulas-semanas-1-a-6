# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 36

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
