# Semana 6 | Slide 13 | Bloco 1
class Cliente:
    """Representa um cliente da empresa."""

    def __init__(self, nome, email, cpf):
        """Construtor: inicializa os atributos."""
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def exibir(self):
        """Exibe os dados do cliente."""
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"CPF: {self.cpf}")

# Criação de objetos
ana = Cliente("Ana Silva", "ana@email.com", "123.456.789-00")
bruno = Cliente("Bruno Costa", "bruno@email.com", "987.654.321-00")

# Uso dos objetos
ana.exibir()
print("---")
bruno.exibir()
