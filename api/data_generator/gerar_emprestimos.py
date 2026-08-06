from datetime import date, timedelta
import random

from config_gerador import *
from helpers import com_chance, talvez_none, enviar

FINALIDADES = [
    "Compra de casa", "Compra de carro", "Negócio próprio", "Educação",
    "Saúde", "Eletrodomésticos", "Viagem", "Obras/reparações",
    "Casamento", "Mobília", "Agricultura", "Comércio", None,
]


def gerar_emprestimos(total, contas, api_url):
    emprestimos = []

    for _ in range(total):
        conta = random.choice(contas) if contas else None
        if com_chance(CHANCE_EMPRESTIMO_CONTA_NULA):
            conta = None

        inicio = date.today() - timedelta(days=random.randint(30, 3000))
        fim = inicio + timedelta(days=random.choice([180, 365, 540, 730, 1095, 1460, 1825]))

        # ~4% com data de fim antes do início (dados inconsistentes)
        if com_chance(CHANCE_DATA_FIM_ANTES):
            fim = inicio - timedelta(days=random.randint(1, 90))

        data = {
            "conta": conta,
            "valor": talvez_none(round(random.uniform(20000, 15000000), 2), CHANCE_VALOR_NULO),
            "taxa_juros": talvez_none(round(random.uniform(2, 24), 2), CHANCE_TAXA_NULA),
            "data_inicio": talvez_none(inicio.isoformat(), CHANCE_DATAS_NULAS),
            "data_fim": talvez_none(fim.isoformat(), CHANCE_DATAS_NULAS),
            "parcelas": talvez_none(random.choice([6, 12, 18, 24, 36, 48, 60]), CHANCE_PARCELAS_NULAS),
            "valor_parcela": talvez_none(round(random.uniform(5000, 500000), 2), CHANCE_VALOR_NULO),
            "finalidade": talvez_none(random.choice(FINALIDADES), CHANCE_FINALIDADE_NULA),
            "status": random.choice(["PENDENTE", "PENDENTE", "APROVADO", "APROVADO", "QUITADO", "REJEITADO"]),
        }

        novo_id = enviar(api_url, "emprestimos", data)
        if novo_id:
            emprestimos.append(novo_id)

    return emprestimos
