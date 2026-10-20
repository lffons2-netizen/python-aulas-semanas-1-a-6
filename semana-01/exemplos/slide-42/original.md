# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 42

```python
nome = input("Primeiro nome: ").strip().capitalize()
sobrenome = input("Sobrenome: ").strip().capitalize()
completo = f"{nome} {sobrenome}"
print(f"Nome formatado: {completo}")
print(f"Iniciais: {nome[0]}.{sobrenome[0]}.")
```
