import csv
from apoio import DadosInvalidosError, executar, validar

def processar(caminho):
    """Lê clientes CSV, valida email/CPF/telefone/data e separa registros inválidos."""
    clientes, invalidos = [], []
    with open(caminho, "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        obrigatorias = {'nome', 'email', 'data', 'cpf', 'telefone'}
        if not obrigatorias.issubset(leitor.fieldnames or []):
            raise DadosInvalidosError("Colunas obrigatórias ausentes no CSV.")
        for numero, linha in enumerate(leitor, start=2):
            try:
                if not (linha.get("nome") or "").strip():
                    raise DadosInvalidosError("Nome obrigatório.")
                validar("email", linha.get("email", ""))
                validar("cpf", linha.get("cpf", ""))
                validar("telefone", linha.get("telefone", ""))
                validar("data", linha.get("data", ""))
            except DadosInvalidosError as erro:
                invalidos.append({"linha": numero, "erro": str(erro)})
            else:
                clientes.append(linha)
    return {"total_validos": len(clientes), "total_invalidos": len(invalidos), "clientes": clientes, "invalidos": invalidos}

if __name__ == "__main__":
    executar("clientes.csv", "clientes.json", processar)
