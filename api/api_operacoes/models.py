from django.db import models

class Cliente(models.Model):
    primeiro_nome = models.CharField(max_length=100, verbose_name="Primeiro Nome")
    ultimo_nome = models.CharField(max_length=100, verbose_name="Último Nome")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Email")
    telefone = models.CharField(max_length=15, verbose_name="Telefone", blank=True)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome} - {self.email}"

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

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contas')
    numero_conta = models.CharField(max_length=20, unique=True)
    tipo_conta = models.CharField(max_length=20, choices=TIPO_CONTA_CHOICES, default='CORRENTE')
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    limite = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    data_abertura = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ATIVA')

    def __str__(self):
        return f"Conta {self.numero_conta} - {self.cliente.primeiro_nome} {self.cliente.ultimo_nome}"


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADO', 'Aprovado'),
        ('REJEITADO', 'Rejeitado'),
        ('QUITADO', 'Quitado'),
    ]

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='emprestimos')
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    taxa_juros = models.DecimalField(max_digits=5, decimal_places=2)  # Ex: 5.50 para 5.5%
    data_inicio = models.DateField()
    data_fim = models.DateField()
    parcelas = models.IntegerField()
    valor_parcela = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')

    def __str__(self):
        return f"Empréstimo R$ {self.valor} - Conta {self.conta.numero_conta}"


class Pagamento(models.Model):
    CATEGORIA_CHOICES = [
        ('ENERGIA', 'Energia'),
        ('AGUA', 'Água'),
        ('INTERNET', 'Internet'),
        ('SALARIO', 'Salário'),
        ('IMPOSTOS', 'Impostos'),
    ]

    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDO', 'Concluído'),
        ('FALHOU', 'Falhou'),
    ]

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='pagamentos')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')

    def __str__(self):
        return f"Pagamento {self.categoria} - R$ {self.valor}"


class Transferencia(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDA', 'Concluída'),
        ('FALHOU', 'Falhou'),
        ('CANCELADA', 'Cancelada'),
    ]

    conta_origem = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transferencias_enviadas')
    conta_destino = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transferencias_recebidas')
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data_transferencia = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')

    def __str__(self):
        return f"Transferência R$ {self.valor} ({self.conta_origem.numero_conta} -> {self.conta_destino.numero_conta})"