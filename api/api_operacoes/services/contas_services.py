from ..models import Conta, Cliente
from .utils import decimal_flexivel, datahora_flexivel, normalizar_texto


class ContaService:

    @staticmethod
    def criar_conta(data):
        try:
            cliente_id = getattr(data, 'cliente', None)
            cliente = None
            if cliente_id:
                try:
                    cliente = Cliente.objects.get(id=cliente_id)
                except (Cliente.DoesNotExist, ValueError, TypeError):
                    cliente = None

            numero_conta = normalizar_texto(getattr(data, 'numero_conta', None))
            if not numero_conta:
                numero_conta = f"ORION{Conta.objects.count() + 1:08d}"

            conta = Conta.objects.create(
                cliente=cliente,
                numero_conta=numero_conta,
                iban=normalizar_texto(getattr(data, 'iban', None)),
                tipo_conta=normalizar_texto(getattr(data, 'tipo_conta', None)),
                saldo=decimal_flexivel(getattr(data, 'saldo', None)),
                limite=decimal_flexivel(getattr(data, 'limite', None)),
                moeda=normalizar_texto(getattr(data, 'moeda', None)),
                data_abertura=datahora_flexivel(getattr(data, 'data_abertura', None)),
                status=normalizar_texto(getattr(data, 'status', None)),
            )
            return conta

        except Exception as e:
            raise ValueError(f"Erro ao criar conta: {str(e)}")
