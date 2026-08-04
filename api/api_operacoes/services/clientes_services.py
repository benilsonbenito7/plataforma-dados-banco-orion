from ..models import Cliente

class ClienteService:
    
    @staticmethod
    def criar_cliente(data):
        try:
            cliente = Cliente.objects.create(
                primeiro_nome=data.primeiro_nome,
                ultimo_nome=data.ultimo_nome,
                email=data.email,
                telefone=data.telefone,
                data_nascimento=data.data_nascimento
            )
            return cliente
        
        except Exception as e:
            raise ValueError(f"Erro ao criar cliente: {str(e)}")