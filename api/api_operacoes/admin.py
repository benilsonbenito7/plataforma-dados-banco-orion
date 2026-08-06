from django.contrib import admin
from .models import Cliente, Conta, Emprestimo, Pagamento, Transferencia

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Conta)
admin.site.register(Emprestimo)
admin.site.register(Pagamento)
admin.site.register(Transferencia)
