from sqlalchemy import create_engine, text
from decouple import config
from ..utils.logger import log_info, log_error


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{config('DB_USER')}:"
    f"{config('DB_PASS')}"
    f"@"
    f"{config('DB_HOST')}:"
    f"{config('DB_PORT')}/"
    f"{config('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT 1"))
        log_info(f"Conexão com o banco de dados bem-sucedida! {resultado.fetchone()[0]}")
except Exception as e:
    log_error(f"Erro ao conectar com o banco de dados: {e}")
    raise