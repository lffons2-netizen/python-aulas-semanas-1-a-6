# Semana 5 | Slide 9 | Bloco 1
# Notas de alunos
notas = [7.5, 9.0, 6.0, 8.5, 10.0]

# Tupla de estatísticas (imutável)
estatisticas = (min(notas), max(notas), sum(notas) / len(notas))
print(f"Mínimo: {estatisticas[0]}")
print(f"Máximo: {estatisticas[1]}")
print(f"Média: {estatisticas[2]:.2f}")
