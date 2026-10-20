from exercicio5_produtos import ProdutoFisico, ProdutoDigital

# Semana 6 | Slide 32 | Bloco 2
produtos = [
    ProdutoFisico("Notebook", 2500, 50),
    ProdutoDigital("Curso Python", 200),
    ProdutoFisico("Mouse", 45.90, 15),
]
for p in produtos:
    print(p)
