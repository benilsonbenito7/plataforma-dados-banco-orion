from ..models import Transferencia, Conta
from decimal import Decimal

class TransferenciaService:
    
    @staticmethod
    def criar_transferencia(data):
        try:
            # Validar contas
            conta_origem = Conta.objects.get(id=data.conta_origem)
            conta_destino = Conta.objects.get(id=data.conta_destino)
            
            # Validar valor
            if data.valor <= 0:
                raise ValueError("Valor da transferência deve ser maior que zero")
            
            # Regra: Não permitir transferência para a mesma conta
            if data.conta_origem == data.conta_destino:
                raise ValueError("Não é permitido transferir para a mesma conta")
            
            # Regra: Validar se conta de origem está ativa
            if conta_origem.status != 'ATIVA':
                raise ValueError("Conta de origem não está ativa")
            
            # Regra: Validar se conta de destino está ativa
            if conta_destino.status != 'ATIVA':
                raise ValueError("Conta de destino não está ativa")
            
            transferencia = Transferencia.objects.create(
                conta_origem=conta_origem,
                conta_destino=conta_destino,
                valor=Decimal(str(data.valor))
            )
            return transferencia
        
        except Conta.DoesNotExist:
            raise ValueError("Uma ou ambas as contas não foram encontradas")
        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError(f"Erro ao criar transferência: {str(e)}")
