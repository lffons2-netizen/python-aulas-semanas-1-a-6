from processar_cadastros import processar_cadastros

from cadastro import validar_email, validar_cpf

# Semana 6 | Slide 6 | Bloco 2
v, inv = processar_cadastros("clientes.txt")
print(f"Válidos: {len(v)}")
print(f"Inválidos: {len(inv)}")
for c in v:
    print(f"    {c['nome']} - {c['email']}")
for c in inv:
    print(f"    {c['nome']} - {c['motivo']}")
