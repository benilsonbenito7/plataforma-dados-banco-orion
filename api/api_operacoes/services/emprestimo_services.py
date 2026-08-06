from ..models import Emprestimo, Conta
from decimal import Decimal
from datetime import datetime

class EmpreistimoService:
    
    @staticmethod
    def criar_emprestimo(data):
        try:
            # Validar conta
            conta = Conta.objects.get(id=data.conta)
            
            # Validar valor
            if data.valor <= 0:
                raise ValueError("Valor do empréstimo deve ser maior que zero")
            
            # Validar taxa de juros
            if data.taxa_juros < 0 or data.taxa_juros > 100:
                raise ValueError("Taxa de juros deve estar entre 0 e 100")
            
            # Validar datas
            data_inicio = datetime.strptime(data.data_inicio, "%Y-%m-%d").date()
            data_fim = datetime.strptime(data.data_fim, "%Y-%m-%d").date()
            
            if data_fim <= data_inicio:
                raise ValueError("Data de fim deve ser posterior à data de início")
            
            # Validar parcelas
            if data.parcelas <= 0:
                raise ValueError("Número de parcelas deve ser maior que zero")
            
            # Calcular valor da parcela (com juros simples)
            juros = Decimal(str(data.valor)) * Decimal(str(data.taxa_juros)) / Decimal('100')
            valor_total = Decimal(str(data.valor)) + juros
            valor_parcela = valor_total / Decimal(str(data.parcelas))
            
            emprestimo = Emprestimo.objects.create(
                conta=conta,
                valor=Decimal(str(data.valor)),
                taxa_juros=Decimal(str(data.taxa_juros)),
                data_inicio=data_inicio,
                data_fim=data_fim,
                parcelas=data.parcelas,
                valor_parcela=valor_parcela
            )
            return emprestimo
        
        except Conta.DoesNotExist:
            raise ValueError("Conta não encontrada")
        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError(f"Erro ao criar empréstimo: {str(e)}")
