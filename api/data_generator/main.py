from config import *

from gerar_clientes import gerar_clientes
from gerar_contas import gerar_contas
from gerar_emprestimos import gerar_emprestimos
from gerar_pagamentos import gerar_pagamentos
from gerar_transferencias import gerar_transferencias



print("🚀 Banco Orion Data Generator")


clientes = gerar_clientes(
    TOTAL_CLIENTES,
    API_URL
)


print(
    "Clientes:",
    len(clientes)
)



contas = gerar_contas(
    TOTAL_CONTAS,
    clientes,
    API_URL
)


print(
    "Contas:",
    len(contas)
)



emprestimos = gerar_emprestimos(
    TOTAL_EMPRESTIMOS,
    contas,
    API_URL
)


print(
    "Empréstimos:",
    len(emprestimos)
)



pagamentos = gerar_pagamentos(
    TOTAL_PAGAMENTOS,
    contas,
    API_URL
)


print(
    "Pagamentos:",
    len(pagamentos)
)



transferencias = gerar_transferencias(
    TOTAL_TRANSFERENCIAS,
    contas,
    API_URL
)


print(
    "Transferências:",
    len(transferencias)
)



print("✅ Carga finalizada")