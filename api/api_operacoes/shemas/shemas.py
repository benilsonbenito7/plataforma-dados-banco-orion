from ninja import schema
from ninja.orm import ModelSchema
from ..models import Cliente, Conta, Emprestimo, Pagamento, Transferencia
from typing import Optional

# ===== CLIENTE SCHEMAS =====
class ClienteSchemaOut(ModelSchema):
    class Meta:
        model = Cliente
        fields = ['id', 'primeiro_nome', 'ultimo_nome', 'email', 'telefone', 'data_nascimento', 'data_criacao']

class ClienteSchemaIn(schema.Schema):
    primeiro_nome: str
    ultimo_nome: str
    email: str
    telefone: Optional[str] = None
    data_nascimento: Optional[str] = None

# ===== CONTA SCHEMAS =====
class ContaSchemaOut(ModelSchema):
    class Meta:
        model = Conta
        fields = ['id', 'cliente', 'numero_conta', 'tipo_conta', 'saldo', 'limite', 'data_abertura', 'status']

class ContaSchemaIn(schema.Schema):
    cliente: int
    numero_conta: str
    tipo_conta: str
    saldo: float = 0.00
    limite: float = 0.00

# ===== EMPRESTIMO SCHEMAS =====
class EmpreistimoSchemaOut(ModelSchema):
    class Meta:
        model = Emprestimo
        fields = ['id', 'conta', 'valor', 'taxa_juros', 'data_inicio', 'data_fim', 'parcelas', 'valor_parcela', 'status']

class EmpreistimoSchemaIn(schema.Schema):
    conta: int
    valor: float
    taxa_juros: float
    data_inicio: str
    data_fim: str
    parcelas: int

# ===== PAGAMENTO SCHEMAS =====
class PagamentoSchemaOut(ModelSchema):
    class Meta:
        model = Pagamento
        fields = ['id', 'conta', 'descricao', 'valor', 'data_pagamento', 'categoria', 'status']

class PagamentoSchemaIn(schema.Schema):
    conta: int
    descricao: str
    valor: float
    categoria: str

# ===== TRANSFERENCIA SCHEMAS =====
class TransferenciaSchemaOut(ModelSchema):
    class Meta:
        model = Transferencia
        fields = ['id', 'conta_origem', 'conta_destino', 'valor', 'data_transferencia', 'status']

class TransferenciaSchemaIn(schema.Schema):
    conta_origem: int
    conta_destino: int
    valor: float
    status: Optional[str] = None