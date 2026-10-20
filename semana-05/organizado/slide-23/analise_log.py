# Semana 5 | Slide 23
# Organização: Painéis do mesmo slide reunidos em ordem.
import re

def analisar_log(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
        return
    except PermissionError:
        print(f"Sem permissão para ler {caminho}.")
        return
    else:
        padrao_ip = r"\d{1,3}(?:\.\d{1,3}){3}"
        padrao_data = r"\d{4}-\d{2}-\d{2}"
        ips = []
        datas = []
        for linha in linhas:
            ips.extend(re.findall(padrao_ip, linha))
            datas.extend(re.findall(padrao_data, linha))

        print(f"Total de linhas: {len(linhas)}")
        print(f"IPs únicos: {len(set(ips))}")
        print(f"Datas encontradas: {len(set(datas))}")
        print(f"IPs: {set(ips)}")
    finally:
        print("Análise concluída.")

# Executar
analisar_log("acesso.log")
