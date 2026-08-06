from ..models import Transferencia, Conta
from .utils import decimal_flexivel, datahora_flexivel, normalizar_texto


class TransferenciaService:

    @staticmethod
    def criar_transferencia(data):
        try:
            origem_id = getattr(data, 'conta_origem', None)
            destino_id = getattr(data, 'conta_destino', None)

            conta_origem = None
            conta_destino = None
            if origem_id:
                try:
                    conta_origem = Conta.objects.get(id=origem_id)
                except (Conta.DoesNotExist, ValueError, TypeError):
                    conta_origem = None
            if destino_id:
                try:
                    conta_destino = Conta.objects.get(id=destino_id)
                except (Conta.DoesNotExist, ValueError, TypeError):
                    conta_destino = None

            transferencia = Transferencia.objects.create(
                conta_origem=conta_origem,
                conta_destino=conta_destino,
                valor=decimal_flexivel(getattr(data, 'valor', None)),
                data_transferencia=datahora_flexivel(getattr(data, 'data_transferencia', None)),
                descricao=normalizar_texto(getattr(data, 'descricao', None)),
                status=normalizar_texto(getattr(data, 'status', None)),
            )
            return transferencia

        except Exception as e:
            raise ValueError(f"Erro ao criar transferência: {str(e)}")
