from ..models import Emprestimo, Conta
from .utils import decimal_flexivel, inteiro_flexivel, data_flexivel, normalizar_texto


class EmpreistimoService:

    @staticmethod
    def criar_emprestimo(data):
        try:
            conta_id = getattr(data, 'conta', None)
            conta = None
            if conta_id:
                try:
                    conta = Conta.objects.get(id=conta_id)
                except (Conta.DoesNotExist, ValueError, TypeError):
                    conta = None

            valor = decimal_flexivel(getattr(data, 'valor', None))
            taxa_juros = decimal_flexivel(getattr(data, 'taxa_juros', None))
            parcelas = inteiro_flexivel(getattr(data, 'parcelas', None))
            valor_parcela = decimal_flexivel(getattr(data, 'valor_parcela', None))

            emprestimo = Emprestimo.objects.create(
                conta=conta,
                valor=valor,
                taxa_juros=taxa_juros,
                data_inicio=data_flexivel(getattr(data, 'data_inicio', None)),
                data_fim=data_flexivel(getattr(data, 'data_fim', None)),
                parcelas=parcelas,
                valor_parcela=valor_parcela,
                finalidade=normalizar_texto(getattr(data, 'finalidade', None)),
                status=normalizar_texto(getattr(data, 'status', None)),
            )
            return emprestimo

        except Exception as e:
            raise ValueError(f"Erro ao criar empréstimo: {str(e)}")
