from django.test import TestCase
from .models import Cliente


class ClienteModelTests(TestCase):
    def test_cliente_pode_ser_criado_sem_telefone_e_email_duplicado(self):
        Cliente.objects.create(
            primeiro_nome="Ana",
            ultimo_nome="Silva",
            email="teste@example.com",
        )

        cliente_duplicado = Cliente.objects.create(
            primeiro_nome="Carlos",
            ultimo_nome="Souza",
            email="teste@example.com",
        )

        self.assertIsNone(cliente_duplicado.telefone)
        self.assertEqual(Cliente.objects.count(), 2)
