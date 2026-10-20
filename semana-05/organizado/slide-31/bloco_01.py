# Contexto: Módulo re e email usados no exemplo do slide 18.
import re
email = "ana@email.com"

# Semana 5 | Slide 31 | Bloco 1
re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)
