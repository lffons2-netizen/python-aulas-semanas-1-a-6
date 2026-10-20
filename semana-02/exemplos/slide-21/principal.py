import runpy

arquivos = []
for indice, arquivo in enumerate(arquivos, start=1):
    print(f"{indice} - {arquivo}")
opcao = int(input("Escolha o exemplo: "))
if 1 <= opcao <= len(arquivos):
    runpy.run_path(arquivos[opcao - 1], run_name="__main__")
else:
    print("Opção inválida.")
