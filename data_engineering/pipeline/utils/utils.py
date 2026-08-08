import pandas as pd
from pathlib import Path
from .logger import log_info

def salvar_dados(cliente: pd.DataFrame, contas: pd.DataFrame, emprestimos: pd.DataFrame, pagamentos: pd.DataFrame, transferencias: pd.DataFrame):
    base_dir = Path(__file__).resolve().parents[2]
    parquet_dir = base_dir / 'output' / 'parquet'

    cliente_dir = parquet_dir / 'clientes'
    cliente_dir.mkdir(parents=True, exist_ok=True)
    cliente.to_parquet(cliente_dir / 'clientes.parquet', index=False)
    log_info("Arquivo clientes.parquet salvo com sucesso!")
    
    contas_dir = parquet_dir / 'contas'
    contas_dir.mkdir(parents=True, exist_ok=True)
    contas.to_parquet(contas_dir / 'contas.parquet', index=False)
    log_info("Arquivo contas.parquet salvo com sucesso!")
    
    emprestimos_dir = parquet_dir / 'emprestimos'
    emprestimos_dir.mkdir(parents=True, exist_ok=True)
    emprestimos.to_parquet(emprestimos_dir / 'emprestimos.parquet', index=False)
    log_info("Arquivo emprestimos.parquet salvo com sucesso!")
    
    pagamentos_dir = parquet_dir / 'pagamentos'
    pagamentos_dir.mkdir(parents=True, exist_ok=True)
    pagamentos.to_parquet(pagamentos_dir / 'pagamentos.parquet', index=False)
    log_info("Arquivo pagamentos.parquet salvo com sucesso!")
    
    transferencias_dir = parquet_dir / 'transferencias'
    transferencias_dir.mkdir(parents=True, exist_ok=True)
    transferencias.to_parquet(transferencias_dir / 'transferencias.parquet', index=False)
    log_info("Arquivo transferencias.parquet salvo com sucesso!")
    