from pandas import read_sql
import pandas as pd
from ..config.database import engine
from ..utils.logger import log_info, log_error

def extract_contas():
    log_info("Iniciando extração de dados das contas ⏳...")
    query = """
           SELECT * FROM api_operacoes_conta
    """
    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        log_error(f"Erro ao extrair dados das contas: {e}")
        return None
    return df