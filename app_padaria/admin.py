from django.contrib import admin
from app_padaria.models import Fornecedor, Cliente, Recebimento


admin.site.register(Fornecedor)
admin.site.register(Cliente)
admin.site.register(Recebimento)