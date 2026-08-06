from datetime import datetime, timedelta
import random

from config_gerador import *
from helpers import com_chance, talvez_none, enviar

DESCRICOES = [
    "Transferência entre contas", "Pagamento de fornecedor",
    "Envio para família", "Compra online", "Aluguer",
    "Reembolso", "Transferência bancária", None,
]


def gerar_transferencias(total, contas, api_url):
    transferencias = []

    for _ in range(total):
        origem = random.choice(contas) if contas else None
        destino = random.choice(contas) if contas else None

        if com_chance(CHANCE_TRANSF_CONTA_NULA):
            origem = None
        if com_chance(CHANCE_TRANSF_CONTA_NULA):
            destino = None

        # ~4% de transferências para a mesma conta (dados anómalos)
        if com_chance(CHANCE_TRANSF_MESMA_CONTA) and origem is not None:
            destino = origem

        data = {
            "conta_origem": origem,
            "conta_destino": destino,
            "valor": talvez_none(round(random.uniform(1000, 8000000), 2), CHANCE_VALOR_NULO),
            "data_transferencia": talvez_none(
                (datetime.now() - timedelta(days=random.randint(0, 1095))).strftime("%Y-%m-%dT%H:%M:%S"),
                CHANCE_DATA_TRANSF_NULA,
            ),
            "descricao": talvez_none(random.choice(DESCRICOES), CHANCE_DESCRICAO_TRANSF_NULA),
            "status": talvez_none(random.choice(["CONCLUIDA", "CONCLUIDA", "PENDENTE", "FALHOU", "CANCELADA"]), CHANCE_STATUS_TRANSF_NULO),
        }

        novo_id = enviar(api_url, "transferencias", data)
        if novo_id:
            transferencias.append(novo_id)

    return transferencias
