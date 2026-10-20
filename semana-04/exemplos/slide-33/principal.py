# Semana 4 | Slide 33 | Bloco 1
# arquivo: principal.py
from adicionar import adicionar
from remover import remover
from atualizar import atualizar
from iterar import iterar
from pertencimento import existe
estoque = ["mouse", "mose", "hd"]
adicionar(estoque, "teclado")
atualizar(estoque, "mose", "mouse2")
remover(estoque, "hd")
if existe(estoque, "teclado"):
    iterar(estoque)  # relatorio final
