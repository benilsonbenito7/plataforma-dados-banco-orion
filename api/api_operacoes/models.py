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