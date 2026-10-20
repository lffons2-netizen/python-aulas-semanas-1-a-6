# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 23

```python
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
```

```python
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
```
