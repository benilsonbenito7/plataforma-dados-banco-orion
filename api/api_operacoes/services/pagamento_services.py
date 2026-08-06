from ..models import Pagamento, Conta
from decimal import Decimal

class PagamentoService:
    
    @staticmethod
    def criar_pagamento(data):
        try:
            # Validar conta
            conta = Conta.objects.get(id=data.conta)
            
            # Validar valor
            if data.valor <= 0:
                raise ValueError("Valor do pagamento deve ser maior que zero")
            
            # Validar categoria
            categorias_validas = ['ENERGIA', 'AGUA', 'INTERNET', 'SALARIO', 'IMPOSTOS']
            if data.categoria not in categorias_validas:
                raise ValueError(f"Categoria inválida. Deve ser: {', '.join(categorias_validas)}")
            
            # Validar descrição
            if not data.descricao or len(data.descricao) < 3:
                raise ValueError("Descrição deve ter no mínimo 3 caracteres")
            
            pagamento = Pagamento.objects.create(
                conta=conta,
                descricao=data.descricao,
                valor=Decimal(str(data.valor)),
                categoria=data.categoria
            )
            return pagamento
        
        except Conta.DoesNotExist:
            raise ValueError("Conta não encontrada")
        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError(f"Erro ao criar pagamento: {str(e)}")
