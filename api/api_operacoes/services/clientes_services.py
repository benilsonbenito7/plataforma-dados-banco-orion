from ..models import Cliente
from .utils import data_flexivel, decimal_flexivel, normalizar_texto


class ClienteService:

    @staticmethod
    def criar_cliente(data):
        try:
            cliente = Cliente.objects.create(
                primeiro_nome=normalizar_texto(getattr(data, 'primeiro_nome', None)),
                ultimo_nome=normalizar_texto(getattr(data, 'ultimo_nome', None)),
                email=normalizar_texto(getattr(data, 'email', None)),
                telefone=normalizar_texto(getattr(data, 'telefone', None)),
                bi=normalizar_texto(getattr(data, 'bi', None)),
                nif=normalizar_texto(getattr(data, 'nif', None)),
                morada=normalizar_texto(getattr(data, 'morada', None)),
                provincia=normalizar_texto(getattr(data, 'provincia', None)),
                municipio=normalizar_texto(getattr(data, 'municipio', None)),
                data_nascimento=data_flexivel(getattr(data, 'data_nascimento', None)),
                genero=normalizar_texto(getattr(data, 'genero', None)),
                estado_civil=normalizar_texto(getattr(data, 'estado_civil', None)),
                profissao=normalizar_texto(getattr(data, 'profissao', None)),
                rendimento_mensal=decimal_flexivel(getattr(data, 'rendimento_mensal', None)),
            )
            return cliente

        except Exception as e:
            raise ValueError(f"Erro ao criar cliente: {str(e)}")
