# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 35

```python
# Exercicio 2: filtrar numeros pares
texto = input("Numeros separados por espaco: ")
numeros = [int(x) for x in texto.split()]
# filtra os divisiveis por 2
pares = [n for n in numeros if n % 2 == 0]
print("Digitados:", numeros)
print("Pares:", pares)
```
