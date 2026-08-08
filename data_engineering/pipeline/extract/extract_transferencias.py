import pandas as pd
from ..config.database import engine
from ..utils.logger import log_info

def extract_transferencias():
    log_info("Iniciando extração de dados das transferências ⏳...")
    query = """
            SELECT * FROM api_operacoes_transferencia
    """
    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        print(f"Erro ao extrair dados das transferências: {e}")
        return None
    return df