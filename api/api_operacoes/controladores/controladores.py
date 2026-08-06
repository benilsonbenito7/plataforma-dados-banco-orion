from ninja import Router
from ..services.clientes_services import ClienteService
from ..services.contas_services import ContaService
from ..services.emprestimo_services import EmpreistimoService
from ..services.pagamento_services import PagamentoService
from ..services.transferencia_services import TransferenciaService
from ..shemas.shemas import (
    ClienteSchemaOut, ClienteSchemaIn,
    ContaSchemaOut, ContaSchemaIn,
    EmpreistimoSchemaOut, EmpreistimoSchemaIn,
    PagamentoSchemaOut, PagamentoSchemaIn,
    TransferenciaSchemaOut, TransferenciaSchemaIn
)

router = Router()

# =================== CLIENTES ===================
@router.post("/clientes", response=ClienteSchemaOut)
def criar_cliente(request, data: ClienteSchemaIn):
    """Inserir novo cliente no banco Orion"""
    return ClienteService.criar_cliente(data)

# =================== CONTAS ===================
@router.post("/contas", response=ContaSchemaOut)
def criar_conta(request, data: ContaSchemaIn):
    """Inserir nova conta no banco Orion"""
    return ContaService.criar_conta(data)

# =================== EMPRÉSTIMOS ===================
@router.post("/emprestimos", response=EmpreistimoSchemaOut)
def criar_emprestimo(request, data: EmpreistimoSchemaIn):
    """Inserir novo empréstimo no banco Orion"""
    return EmpreistimoService.criar_emprestimo(data)

# =================== PAGAMENTOS ===================
@router.post("/pagamentos", response=PagamentoSchemaOut)
def criar_pagamento(request, data: PagamentoSchemaIn):
    """Inserir novo pagamento no banco Orion"""
    return PagamentoService.criar_pagamento(data)

# =================== TRANSFERÊNCIAS ===================
@router.post("/transferencias", response=TransferenciaSchemaOut)
def criar_transferencia(request, data: TransferenciaSchemaIn):
    """Inserir nova transferência no banco Orion"""
    return TransferenciaService.criar_transferencia(data)