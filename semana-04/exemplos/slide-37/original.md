# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 37

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
