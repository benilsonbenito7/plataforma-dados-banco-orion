from ..models import Conta, Cliente
from decimal import Decimal

class ContaService:
    
    @staticmethod
    def criar_conta(data):
        try:
            # Validar cliente
            cliente = Cliente.objects.get(id=data.cliente)
            
            # Validar número de conta único
            if Conta.objects.filter(numero_conta=data.numero_conta).exists():
                raise ValueError("Número de conta já existe")
            
            # Validar tipo de conta
            tipos_validos = ['CORRENTE', 'POUPANCA', 'INVESTIMENTO']
            if data.tipo_conta not in tipos_validos:
                raise ValueError(f"Tipo de conta inválido. Deve ser: {', '.join(tipos_validos)}")
            
            conta = Conta.objects.create(
                cliente=cliente,
                numero_conta=data.numero_conta,
                tipo_conta=data.tipo_conta,
                saldo=Decimal(str(data.saldo)),
                limite=Decimal(str(data.limite))
            )
            return conta
        
        except Cliente.DoesNotExist:
            raise ValueError("Cliente não encontrado")
        except Exception as e:
            raise ValueError(f"Erro ao criar conta: {str(e)}")
