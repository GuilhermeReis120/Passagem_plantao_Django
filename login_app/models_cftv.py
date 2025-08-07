from django.db import models


class PassageCFTV(models.Model):
    data = models.DateTimeField()
    operador = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    nome_backoffice = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)  # Salva o horário de envio
    # Adicione outros campos específicos do CFTV conforme necessário

    def __str__(self):
        return f"{self.data} - {self.operador} - {self.base}"
