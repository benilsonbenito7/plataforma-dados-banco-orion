from .extract.extract_clientes import extract_clientes
from .extract.extract_contas import extract_contas
from .extract.extract_emprestimos import extract_emprestimos
from .extract.extract_pagamentos import extract_pagamentos
from .extract.extract_transferencias import extract_transferencias
from .utils.utils import salvar_dados
from .utils.logger import log_info

def main():
    cliente = extract_clientes()
    log_info(f'Clientes: {cliente.shape} dados extraídos com sucesso!')

    contas = extract_contas()
    log_info(f'Contas: {contas.shape} dados extraídos com sucesso!')

    emprestimos = extract_emprestimos()
    log_info(f'Emprestimos: {emprestimos.shape} dados extraídos com sucesso!')

    pagamentos = extract_pagamentos()
    log_info(f'Pagamentos: {pagamentos.shape} dados extraídos com sucesso!')

    transferencias = extract_transferencias()
    log_info(f'Transferencias: {transferencias.shape} dados extraídos com sucesso!')
    
    salvar_dados(cliente, contas, emprestimos, pagamentos, transferencias)

if __name__ == "__main__":
    main()
