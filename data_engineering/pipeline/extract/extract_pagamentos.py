import pandas as pd
from ..config.database import engine
from ..utils.logger import log_info

def extract_pagamentos():
    log_info("Iniciando extração de dados das pagamentos ⏳...")
    query = """
           SELECT * FROM api_operacoes_pagamento
    """
    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        print(f"Erro ao extrair dados das pagamentos: {e}")
        return None
    return df