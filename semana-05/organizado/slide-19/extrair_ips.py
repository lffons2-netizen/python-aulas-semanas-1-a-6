# Semana 5 | Slide 19 | Bloco 1
import re


log = """
2026-08-30 10:00:00 192.168.1.1 GET /index.html
2026-08-30 10:05:00 10.0.0.5 POST /login
2026-08-30 10:10:00 192.168.1.1 GET /dashboard
"""

padrao_ip = r"\d{1,3}(?:\.\d{1,3}){3}"
ips = re.findall(padrao_ip, log)
print(ips)  # ['192.168.1.1', '10.0.0.5', '192.168.1.1']

# IPs únicos
print(set(ips))  # {'192.168.1.1', '10.0.0.5'}
