# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 38

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
