# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 47

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
