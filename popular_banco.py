import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_projeto.settings')
django.setup()

from login_app.models_plantao import CentralMonitoramento
from django.contrib.auth.models import User

bases = ['base1', 'base2', 'base3', 'base4']
usuarios = [f'user{i+1}' for i in range(15)]
backoffices = [f'Backoffice {i+1}' for i in range(15)]

start_date = datetime.now() - timedelta(days=30)

for dia in range(30):
    data_atual = start_date + timedelta(days=dia)
    for idx, usuario in enumerate(usuarios):
        base = random.choice(bases)
        nome_backoffice = backoffices[idx]
        for _ in range(random.randint(1, 3)):
            CentralMonitoramento.objects.using('plantao_db').create(
                data=data_atual.strftime('%Y-%m-%d'),
                plantao=random.choice(['Manhã', 'Tarde', 'Noite']),
                base=base,
                total_veiculos=random.randint(10, 50),
                veiculos_pernoite=random.randint(0, 10),
                veiculos_viagem=random.randint(0, 10),
                veiculos_manutencao=random.randint(0, 5),
                veiculos_cliente=random.randint(0, 5),
                desvios_rota=random.randint(0, 2),
                rotas_embarcadas=random.randint(0, 10),
                veiculos_para_iniciar_viagem=random.randint(0, 5),
                veiculos_postos_fiscais=random.randint(0, 3),
                veiculos_borracharias=random.randint(0, 2),
                sinistros=random.randint(0, 2),
                parada_nao_autorizada=random.randint(0, 1),
                veiculos_abandonados=random.randint(0, 1),
                veiculos_bloqueados_inatividade=random.randint(0, 2),
                perda_sinal=random.randint(0, 1),
                rotas_embarcadas_3s=random.randint(0, 5),
                rotas_embarcadas_t4s=random.randint(0, 5),
                tem_mouse_pad=random.choice([True, False]),
                tem_descanso_pe=random.choice([True, False]),
                tem_carregador=random.choice([True, False]),
                observacoes='Teste automático',
                usuario=usuario,
                nome_backoffice=nome_backoffice,
                nome_usuario=usuario,
            )
print('Banco populado com sucesso!')
