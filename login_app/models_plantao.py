# Model para salvar passagem de plantão em outro banco
from django.db import models
from django.conf import settings

class PassagemPlantao(models.Model):
    # Data do registro
    data = models.DateField()
    # Plantão (pode ser texto ou escolha)
    plantao = models.CharField(max_length=100)
    # Base (pode ser texto ou escolha)
    base = models.CharField(max_length=100)
    # Campos principais do formulário
    total_veiculos = models.IntegerField()
    veiculos_pernoite = models.IntegerField()
    veiculos_viagem = models.IntegerField()
    veiculos_manutencao = models.IntegerField()
    veiculos_cliente = models.IntegerField()
    tentativas_roubo = models.IntegerField()
    roubos_consolidados = models.IntegerField()
    acidentes = models.IntegerField()
    desvios_rota = models.IntegerField()
    observacoes = models.TextField(blank=True)

    class Meta:
        app_label = 'login_app'  # Para o router identificar

class CentralMonitoramento(models.Model):
    data = models.DateField()
    data_envio = models.DateTimeField(auto_now_add=True)  # Salva o horário de envio
    plantao = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    total_veiculos = models.IntegerField()
    veiculos_pernoite = models.IntegerField()
    veiculos_viagem = models.IntegerField()
    veiculos_manutencao = models.IntegerField()
    veiculos_cliente = models.IntegerField()
    desvios_rota = models.IntegerField()
    rotas_embarcadas = models.IntegerField(default=0)
    veiculos_para_iniciar_viagem = models.IntegerField(default=0)
    veiculos_postos_fiscais = models.IntegerField(default=0)
    veiculos_borracharias = models.IntegerField(default=0)
    sinistros = models.IntegerField(default=0)
    parada_nao_autorizada = models.IntegerField(default=0)
    veiculos_abandonados = models.IntegerField(default=0)
    veiculos_bloqueados_inatividade = models.IntegerField(default=0)
    perda_sinal = models.IntegerField(default=0)
    rotas_embarcadas_3s = models.IntegerField(default=0)
    rotas_embarcadas_t4s = models.IntegerField(default=0)
    tem_mouse_pad = models.BooleanField(default=False)
    tem_descanso_pe = models.BooleanField(default=False)
    tem_carregador = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True)
    usuario = models.CharField(max_length=150, blank=True, null=True)
    nome_coordenador = models.CharField(max_length=150, blank=True, null=True)
    nome_usuario = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        app_label = 'login_app'
        db_table = 'centralMonitoramento'  # Define o nome da tabela
