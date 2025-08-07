import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_projeto.settings')
django.setup()

from login_app.models_plantao import CentralMonitoramento

# Apaga todos os registros da tabela CentralMonitoramento no banco plantao_db
CentralMonitoramento.objects.using('plantao_db').all().delete()

print('Todos os dados da tabela CentralMonitoramento foram removidos do banco plantao_db.')
