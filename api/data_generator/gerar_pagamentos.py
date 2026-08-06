from datetime import datetime, timedelta
import random

from config_gerador import *
from helpers import com_chance, talvez_none, enviar

CATEGORIAS = ["ENERGIA", "AGUA", "INTERNET", "SALARIO", "IMPOSTOS", "SAUDE", "EDUCACAO", "TRANSPORTE", "COMERCIO", "OUTROS"]

DESCRICOES = [
    "Pagamento mensal de energia", "Conta de água", "Internet e TV",
    "Salário", "Impostos", "Consulta médica", "Propinas",
    "Transporte público", "Compra no supermercado", "Pagamento de serviços",
    "Recarga", "Multa", "Mensalidade", None,
]


def gerar_pagamentos(total, contas, api_url):
    pagamentos = []

    for _ in range(total):
        conta = random.choice(contas) if contas else None
        if com_chance(CHANCE_PAGAMENTO_CONTA_NULA):
            conta = None

        categoria = talvez_none(random.choice(CATEGORIAS), CHANCE_CATEGORIA_NULA)
        if com_chance(CHANCE_CATEGORIA_DESCONHECIDA):
            categoria = random.choice(["LAZER", "JOGOS", "CRIPTO", "EXTRAS", "TOKEN123"])

        data = {
            "conta": conta,
            "descricao": talvez_none(random.choice(DESCRICOES), CHANCE_DESCRICAO_NULA),
            "valor": talvez_none(round(random.uniform(500, 2500000), 2), CHANCE_VALOR_NULO),
            "data_pagamento": talvez_none(
                (datetime.now() - timedelta(days=random.randint(0, 1095))).strftime("%Y-%m-%dT%H:%M:%S"),
                CHANCE_DATA_PAG_NULA,
            ),
            "categoria": categoria,
            "status": talvez_none(random.choice(["CONCLUIDO", "CONCLUIDO", "PENDENTE", "FALHOU", "CANCELADO"]), CHANCE_STATUS_PAG_NULO),
        }

        novo_id = enviar(api_url, "pagamentos", data)
        if novo_id:
            pagamentos.append(novo_id)

    return pagamentos
