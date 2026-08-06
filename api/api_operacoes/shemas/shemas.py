from ninja import schema
from ninja.orm import ModelSchema
from ..models import Cliente, Conta, Emprestimo, Pagamento, Transferencia
from typing import Optional

# ===== CLIENTE SCHEMAS =====
class ClienteSchemaOut(ModelSchema):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteSchemaIn(schema.Schema):
    primeiro_nome: Optional[str] = None
    ultimo_nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    bi: Optional[str] = None
    nif: Optional[str] = None
    morada: Optional[str] = None
    provincia: Optional[str] = None
    municipio: Optional[str] = None
    data_nascimento: Optional[str] = None
    genero: Optional[str] = None
    estado_civil: Optional[str] = None
    profissao: Optional[str] = None
    rendimento_mensal: Optional[float] = None

# ===== CONTA SCHEMAS =====
class ContaSchemaOut(ModelSchema):
    class Meta:
        model = Conta
        fields = '__all__'

class ContaSchemaIn(schema.Schema):
    cliente: Optional[int] = None
    numero_conta: Optional[str] = None
    iban: Optional[str] = None
    tipo_conta: Optional[str] = None
    saldo: Optional[float] = None
    limite: Optional[float] = None
    moeda: Optional[str] = None
    data_abertura: Optional[str] = None
    status: Optional[str] = None

# ===== EMPRESTIMO SCHEMAS =====
class EmpreistimoSchemaOut(ModelSchema):
    class Meta:
        model = Emprestimo
        fields = '__all__'

class EmpreistimoSchemaIn(schema.Schema):
    conta: Optional[int] = None
    valor: Optional[float] = None
    taxa_juros: Optional[float] = None
    data_inicio: Optional[str] = None
    data_fim: Optional[str] = None
    parcelas: Optional[int] = None
    valor_parcela: Optional[float] = None
    finalidade: Optional[str] = None
    status: Optional[str] = None

# ===== PAGAMENTO SCHEMAS =====
class PagamentoSchemaOut(ModelSchema):
    class Meta:
        model = Pagamento
        fields = '__all__'

class PagamentoSchemaIn(schema.Schema):
    conta: Optional[int] = None
    descricao: Optional[str] = None
    valor: Optional[float] = None
    data_pagamento: Optional[str] = None
    categoria: Optional[str] = None
    status: Optional[str] = None

# ===== TRANSFERENCIA SCHEMAS =====
class TransferenciaSchemaOut(ModelSchema):
    class Meta:
        model = Transferencia
        fields = '__all__'

class TransferenciaSchemaIn(schema.Schema):
    conta_origem: Optional[int] = None
    conta_destino: Optional[int] = None
    valor: Optional[float] = None
    data_transferencia: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[str] = None
