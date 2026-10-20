import json
import re
from datetime import date

class DadosInvalidosError(ValueError):
    """Indica que um registro não atende às validações do exercício."""

PADROES = {
    "email": r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$",
    "cpf": r"^\d{3}\.\d{3}\.\d{3}-\d{2}$",
    "telefone": r"^\(\d{2}\) \d{4,5}-\d{4}$",
    "data": r"^\d{4}-\d{2}-\d{2}$",
    "cep": r"^\d{5}-\d{3}$",
}

def validar(campo, valor):
    """Valida formato com regex; datas também são conferidas no calendário."""
    if not isinstance(valor, str) or not re.fullmatch(PADROES[campo], valor):
        raise DadosInvalidosError(f"{campo} inválido: {valor}")
    if campo == "data":
        try:
            date.fromisoformat(valor)
        except ValueError as erro:
            raise DadosInvalidosError(f"Data inexistente: {valor}") from erro
    return valor

def executar(entrada, saida, processar):
    """Processa entrada, salva JSON e demonstra try/except/else/finally."""
    try:
        resultado = processar(entrada)
        with open(saida, "w", encoding="utf-8") as arquivo:
            json.dump(resultado, arquivo, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {entrada}")
        return False
    except DadosInvalidosError as erro:
        print(f"Dados inválidos: {erro}")
        return False
    except (ValueError, KeyError, TypeError) as erro:
        print(f"Conteúdo inválido: {erro}")
        return False
    except OSError as erro:
        print(f"Erro de leitura/escrita: {erro}")
        return False
    else:
        print(f"Relatório salvo em {saida}")
        for campo, valor in resultado.items():
            print(f"{campo}: {valor}")
        return True
    finally:
        print("Processamento encerrado.")
