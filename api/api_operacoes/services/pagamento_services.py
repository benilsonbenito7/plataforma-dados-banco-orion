from ..models import Pagamento, Conta
from .utils import decimal_flexivel, datahora_flexivel, normalizar_texto


class PagamentoService:

    @staticmethod
    def criar_pagamento(data):
        try:
            conta_id = getattr(data, 'conta', None)
            conta = None
            if conta_id:
                try:
                    conta = Conta.objects.get(id=conta_id)
                except (Conta.DoesNotExist, ValueError, TypeError):
                    conta = None

            pagamento = Pagamento.objects.create(
                conta=conta,
                descricao=normalizar_texto(getattr(data, 'descricao', None)),
                valor=decimal_flexivel(getattr(data, 'valor', None)),
                data_pagamento=datahora_flexivel(getattr(data, 'data_pagamento', None)),
                categoria=normalizar_texto(getattr(data, 'categoria', None)),
                status=normalizar_texto(getattr(data, 'status', None)),
            )
            return pagamento

        except Exception as e:
            raise ValueError(f"Erro ao criar pagamento: {str(e)}")
