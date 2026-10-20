import re
from apoio import DadosInvalidosError, executar

def processar(caminho):
    """Lê uma nota por linha, valida formato e faixa de zero a dez."""
    notas, invalidas = [], []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, start=1):
            texto = linha.strip()
            try:
                if not re.fullmatch(r"\d+(?:[.,]\d+)?", texto):
                    raise DadosInvalidosError("Use uma nota numérica por linha.")
                nota = float(texto.replace(",", "."))
                if not 0 <= nota <= 10:
                    raise DadosInvalidosError("Nota fora da faixa de zero a dez.")
            except DadosInvalidosError as erro:
                invalidas.append({"linha": numero, "erro": str(erro)})
            else:
                notas.append(nota)
    if not notas:
        raise DadosInvalidosError("Não há notas válidas para calcular a média.")
    return {"notas_validas": notas, "media": round(sum(notas) / len(notas), 2), "invalidas": invalidas}

if __name__ == "__main__":
    executar("notas.txt", "relatorio_notas.json", processar)
