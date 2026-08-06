import random
import requests


def com_chance(chance):
    return random.random() < chance


def talvez_none(valor, chance):
    """Devolve None com uma dada probabilidade (dado em falta)."""
    return None if com_chance(chance) else valor


def talvez_vazio(valor, chance):
    """Devolve string vazia com uma dada probabilidade (dado vazio)."""
    return "" if com_chance(chance) else valor


def sujar_texto(valor, chance_none=0.05, chance_vazio=0.03, chance_caixa=0.05, chance_espacos=0.03):
    """Injeta sujidade típica de bases reais: nulos, vazios, caixa e espaços."""
    if valor is None:
        return valor
    if com_chance(chance_none):
        return None
    if com_chance(chance_vazio):
        return ""
    resultado = str(valor)
    if com_chance(chance_espacos):
        resultado = f" {resultado} "
    if com_chance(chance_caixa):
        resultado = random.choice([resultado.upper(), resultado.lower()])
    return resultado


def enviar(api_url, endpoint, dados):
    """Envia um POST e devolve o id criado ou None em caso de erro."""
    try:
        resposta = requests.post(f"{api_url}/{endpoint}", json=dados, timeout=30)
        if resposta.status_code == 200:
            corpo = resposta.json()
            return corpo.get("id")
        return None
    except Exception as erro:
        print(f"Falha de conexão em /{endpoint}: {erro}")
        return None
