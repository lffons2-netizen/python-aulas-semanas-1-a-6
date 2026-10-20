# Semana 6 | Slide 1 | Bloco 1
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        return self.nota >= 7

print(Aluno("Ana", 8.5).aprovado())  # True
