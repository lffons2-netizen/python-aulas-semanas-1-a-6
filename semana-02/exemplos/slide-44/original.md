# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 44

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
