import csv
import re
from apoio import DadosInvalidosError, executar

def processar(caminho, categoria="Perifericos"):
    """Lê produtos, valida nome/categoria/preço e filtra pela categoria."""
    produtos, invalidos = [], []
    with open(caminho, "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        obrigatorias = {'nome', 'categoria', 'preco'}
        if not obrigatorias.issubset(leitor.fieldnames or []):
            raise DadosInvalidosError("Colunas obrigatórias ausentes no CSV.")
        for numero, linha in enumerate(leitor, start=2):
            try:
                if not (linha.get("nome") or "").strip() or not re.fullmatch(r"[\wÀ-ÿ -]+", (linha.get("categoria") or "")):
                    raise DadosInvalidosError("Nome ou categoria inválido.")
                valor = linha.get("preco") or ""
                if not re.fullmatch(r"\d+(?:\.\d{1,2})?", valor):
                    raise DadosInvalidosError("Preço inválido; use ponto decimal e até duas casas.")
                produto = {"nome": linha["nome"], "categoria": linha["categoria"], "preco": float(valor)}
            except DadosInvalidosError as erro:
                invalidos.append({"linha": numero, "erro": str(erro)})
            else:
                produtos.append(produto)
    filtrados = [p for p in produtos if p["categoria"].casefold() == categoria.casefold()]
    return {"categoria": categoria, "total_validos": len(produtos), "filtrados": filtrados, "invalidos": invalidos}

if __name__ == "__main__":
    categoria = input("Categoria: ").strip()
    executar("produtos.csv", "relatorio_estoque.json", lambda caminho: processar(caminho, categoria))
