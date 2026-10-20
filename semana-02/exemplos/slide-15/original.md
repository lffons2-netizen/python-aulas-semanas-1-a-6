# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 14

```python
# Entrada de dados (com conversão para número real)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
```

## Slide 15

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
