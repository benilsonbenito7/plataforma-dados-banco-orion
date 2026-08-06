from datetime import timedelta
import random

from config_gerador import *
from helpers import com_chance, talvez_none, sujar_texto, enviar


def numero_conta_angola():
    return f"{random.randint(10000000, 99999999)}"


def iban_angola(numero_conta):
    """IBAN angolano: AO + 21 caracteres (ex: AO06 0044 0000 1234 5678 9012 3)."""
    return f"AO{random.randint(10, 99)}{random.randint(100000000, 999999999)}0{numero_conta}"


def saldo_conta():
    if com_chance(CHANCE_SALDO_NEGATIVO):
        return round(-random.uniform(100, 20000), 2)
    return round(random.uniform(0, 2500000), 2)


def gerar_contas(total, clientes, api_url):
    contas = []
    numeros_usados = []

    for _ in range(total):
        numero = numero_conta_angola()

        # ~8% de números de conta duplicados (dados sujos)
        if numeros_usados and com_chance(CHANCE_NUMERO_CONTA_DUPLICADO):
            numero = random.choice(numeros_usados)
        else:
            numeros_usados.append(numero)

        cliente = random.choice(clientes) if clientes else None
        if com_chance(0.03):
            cliente = None

        data = {
            "cliente": cliente,
            "numero_conta": talvez_none(numero, CHANCE_NUMERO_CONTA_NULO),
            "iban": talvez_none(iban_angola(numero), CHANCE_IBAN_NULO),
            "tipo_conta": talvez_none(random.choice(["CORRENTE", "POUPANCA", "INVESTIMENTO"]), CHANCE_TIPO_CONTA_NULO),
            "saldo": talvez_none(saldo_conta(), CHANCE_SALDO_NULO),
            "limite": talvez_none(round(random.uniform(0, 500000), 2), CHANCE_LIMITE_NULO),
            "moeda": "AOA",
            "data_abertura": (__import__("datetime").date.today() - timedelta(days=random.randint(0, 3650))).isoformat(),
            "status": talvez_none(random.choice(["ATIVA", "ATIVA", "ATIVA", "BLOQUEADA", "ENCERRADA"]), CHANCE_STATUS_CONTA_NULO),
        }

        novo_id = enviar(api_url, "contas", data)
        if novo_id:
            contas.append(novo_id)

    return contas
