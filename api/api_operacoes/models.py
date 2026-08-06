from django.db import models


class Cliente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    primeiro_nome = models.CharField(max_length=100, null=True, blank=True, verbose_name="Primeiro Nome")
    ultimo_nome = models.CharField(max_length=100, null=True, blank=True, verbose_name="Último Nome")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="Email")
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone")
    bi = models.CharField(max_length=20, null=True, blank=True, verbose_name="Bilhete de Identidade")
    nif = models.CharField(max_length=20, null=True, blank=True, verbose_name="NIF")
    morada = models.CharField(max_length=255, null=True, blank=True, verbose_name="Morada")
    provincia = models.CharField(max_length=50, null=True, blank=True, verbose_name="Província")
    municipio = models.CharField(max_length=50, null=True, blank=True, verbose_name="Município")
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, null=True, blank=True, verbose_name="Género")
    estado_civil = models.CharField(max_length=20, null=True, blank=True, verbose_name="Estado Civil")
    profissao = models.CharField(max_length=100, null=True, blank=True, verbose_name="Profissão")
    rendimento_mensal = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True, verbose_name="Rendimento Mensal (Kz)")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"{self.primeiro_nome or ''} {self.ultimo_nome or ''} - {self.email or ''}".strip()


class Conta(models.Model):
    TIPO_CONTA_CHOICES = [
        ('CORRENTE', 'Corrente'),
        ('POUPANCA', 'Poupança'),
        ('INVESTIMENTO', 'Investimento'),
    ]

    STATUS_CHOICES = [
        ('ATIVA', 'Ativa'),
        ('BLOQUEADA', 'Bloqueada'),
        ('ENCERRADA', 'Encerrada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contas', null=True, blank=True)
    numero_conta = models.CharField(max_length=20, null=True, blank=True)
    iban = models.CharField(max_length=34, null=True, blank=True, verbose_name="IBAN")
    tipo_conta = models.CharField(max_length=20, choices=TIPO_CONTA_CHOICES, null=True, blank=True)
    saldo = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    limite = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    moeda = models.CharField(max_length=3, null=True, blank=True, default='AOA')
    data_abertura = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Conta {self.numero_conta or ''} - {self.cliente}"


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADO', 'Aprovado'),
        ('REJEITADO', 'Rejeitado'),
        ('QUITADO', 'Quitado'),
    ]

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='emprestimos', null=True, blank=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    taxa_juros = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    parcelas = models.IntegerField(null=True, blank=True)
    valor_parcela = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    finalidade = models.CharField(max_length=100, null=True, blank=True, verbose_name="Finalidade")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Empréstimo Kz {self.valor or 0} - Conta {getattr(self.conta, 'numero_conta', '') or ''}"


class Pagamento(models.Model):
    CATEGORIA_CHOICES = [
        ('ENERGIA', 'Energia'),
        ('AGUA', 'Água'),
        ('INTERNET', 'Internet'),
        ('SALARIO', 'Salário'),
        ('IMPOSTOS', 'Impostos'),
        ('SAUDE', 'Saúde'),
        ('EDUCACAO', 'Educação'),
        ('TRANSPORTE', 'Transporte'),
        ('COMERCIO', 'Comércio'),
        ('OUTROS', 'Outros'),
    ]

    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDO', 'Concluído'),
        ('FALHOU', 'Falhou'),
        ('CANCELADO', 'Cancelado'),
    ]

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='pagamentos', null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    data_pagamento = models.DateTimeField(null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Pagamento {self.categoria or ''} - Kz {self.valor or 0}"


class Transferencia(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDA', 'Concluída'),
        ('FALHOU', 'Falhou'),
        ('CANCELADA', 'Cancelada'),
    ]

    conta_origem = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transferencias_enviadas', null=True, blank=True)
    conta_destino = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transferencias_recebidas', null=True, blank=True)
    valor = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    data_transferencia = models.DateTimeField(null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True, verbose_name="Descrição")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Transferência Kz {self.valor or 0} ({getattr(self.conta_origem, 'numero_conta', '') or ''} -> {getattr(self.conta_destino, 'numero_conta', '') or ''})"
