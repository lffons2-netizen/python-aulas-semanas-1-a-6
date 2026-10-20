from cadastro import validar_email, validar_cpf

# Semana 6 | Slide 7 | Bloco 1
cliente = {"nome": "Ana", "email": "ana@email.com"}

# 1. Nada impede um dicionário inconsistente
cliente["emial"] = "ana@"     # erro de digitação aceito
del cliente["nome"]           # campo obrigatório some

# 2. Dados e regras vivem separados
validar_email(cliente["email"])   # e se alguém esquecer?

# 3. Sem comportamento próprio
cliente.validar()   # AttributeError: 'dict' object
                    # has no attribute 'validar'
