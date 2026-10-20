import csv
from apoio import DadosInvalidosError, executar, validar

def processar(caminho):
    """Valida telefone, data e CEP de cada formulário lido de CSV."""
    validos, invalidos = [], []
    with open(caminho, "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        obrigatorias = {'cep', 'telefone', 'data'}
        if not obrigatorias.issubset(leitor.fieldnames or []):
            raise DadosInvalidosError("Colunas obrigatórias ausentes no CSV.")
        for numero, linha in enumerate(leitor, start=2):
            try:
                for campo in ("telefone", "data", "cep"):
                    validar(campo, linha.get(campo, ""))
            except DadosInvalidosError as erro:
                invalidos.append({"linha": numero, "erro": str(erro)})
            else:
                validos.append(linha)
    return {"total_validos": len(validos), "total_invalidos": len(invalidos), "formularios": validos, "invalidos": invalidos}

if __name__ == "__main__":
    executar("formularios.csv", "formularios.json", processar)
