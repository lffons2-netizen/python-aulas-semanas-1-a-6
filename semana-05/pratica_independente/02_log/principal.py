import ipaddress
import re
from apoio import DadosInvalidosError, executar, validar

def processar(caminho):
    """Extrai IPs, datas e erros; registra linhas malformadas no relatório."""
    ips, datas, erros, invalidas = [], [], [], []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    for numero, linha in enumerate(linhas, start=1):
        if not linha.strip():
            continue
        try:
            ip = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", linha)
            data = re.search(r"\b\d{4}-\d{2}-\d{2}\b", linha)
            if ip is None or data is None:
                raise DadosInvalidosError("Linha sem IP ou data.")
            ipaddress.ip_address(ip.group())
            validar("data", data.group())
        except (DadosInvalidosError, ValueError) as erro:
            invalidas.append({"linha": numero, "erro": str(erro)})
        else:
            ips.append(ip.group())
            datas.append(data.group())
        if re.search(r"\b(ERROR|CRITICAL|Exception|Traceback)\b", linha, re.IGNORECASE):
            erros.append(linha.strip())
    return {"total_linhas": len(linhas), "ips_unicos": sorted(set(ips)), "datas": sorted(set(datas)), "erros": erros, "linhas_invalidas": invalidas}

if __name__ == "__main__":
    executar("acesso.log", "resumo.json", processar)
