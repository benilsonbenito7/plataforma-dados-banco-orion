from pandas import read_sql
import pandas as pd
from ..config.database import engine
from ..utils.logger import log_info, log_error

def extract_clientes():
    log_info("Iniciando extração de dados dos clientes ⏳...")
    query = """
            SELECT * FROM api_operacoes_cliente
    """
    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        log_error(f"Erro ao extrair dados dos clientes: {e}")
        return None
    return df