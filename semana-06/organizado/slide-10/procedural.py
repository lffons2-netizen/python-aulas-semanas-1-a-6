from cadastro import validar_email, validar_cpf

# Semana 6 | Slide 10 | Bloco 1
# Modelo procedural: dados soltos
cliente1 = {"nome": "Ana",
            "email": "ana@email.com",
            "cpf": "123.456.789-00"}
cliente2 = {"nome": "Bruno",
            "email": "bruno@email.com",
            "cpf": "987.654.321-00"}

def validar_cliente(cliente):
    return (validar_email(cliente["email"])
            and validar_cpf(cliente["cpf"]))

def exibir_cliente(cliente):
    print(f"{cliente['nome']} - {cliente['email']}")
