from ninja import schema
from ninja.orm import ModelSchema
from ..models import Cliente

class ClienteSchemaOut(ModelSchema):
    class Meta:
        model = Cliente
        fields = ['id', 'primeiro_nome', 'ultimo_nome', 'email', 'telefone', 'data_nascimento', 'data_criacao']

class ClienteSchemaIn(schema.Schema):
    primeiro_nome: str
    ultimo_nome: str
    email: str
    telefone: str = None
    data_nascimento: str = None