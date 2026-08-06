import time

from config_gerador import *

from gerar_clientes import gerar_clientes
from gerar_contas import gerar_contas
from gerar_emprestimos import gerar_emprestimos
from gerar_pagamentos import gerar_pagamentos
from gerar_transferencias import gerar_transferencias


def cronometrar(funcao, *args):
    inicio = time.time()
    resultado = funcao(*args)
    duracao = round(time.time() - inicio, 2)
    return resultado, duracao


print("=" * 60)
print("Banco Orion - Data Generator (dados realistas angolanos + sujeira)")
print("=" * 60)

clientes, t = cronometrar(gerar_clientes, TOTAL_CLIENTES, API_URL)
print(f"Clientes inseridos: {len(clientes)}  ({t}s)")

contas, t = cronometrar(gerar_contas, TOTAL_CONTAS, clientes, API_URL)
print(f"Contas inseridas: {len(contas)}  ({t}s)")

emprestimos, t = cronometrar(gerar_emprestimos, TOTAL_EMPRESTIMOS, contas, API_URL)
print(f"Emprestimos inseridos: {len(emprestimos)}  ({t}s)")

pagamentos, t = cronometrar(gerar_pagamentos, TOTAL_PAGAMENTOS, contas, API_URL)
print(f"Pagamentos inseridos: {len(pagamentos)}  ({t}s)")

transferencias, t = cronometrar(gerar_transferencias, TOTAL_TRANSFERENCIAS, contas, API_URL)
print(f"Transferencias inseridas: {len(transferencias)}  ({t}s)")

print("=" * 60)
print("Carga finalizada. Os dados contêm nulos, vazios e duplicados de propósito.")
print("Pronto para o pipeline ETL (Databricks): Bronze -> Silver -> Gold")
print("=" * 60)