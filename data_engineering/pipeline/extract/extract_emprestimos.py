import pandas as pd
from ..config.database import engine
from ..utils.logger import log_info, log_error

def extract_emprestimos():
    log_info("Iniciando extração de dados dos emprestimos ⏳...")
    query = """
           SELECT * FROM api_operacoes_emprestimo
    """
    try:
        df = pd.read_sql(query, engine)
    except Exception as e:
        log_error(f"Erro ao extrair dados dos emprestimos: {e}")
        return None
    return df