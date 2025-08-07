# Router para usar outro banco de dados para PassagemPlantao
class PlantaoRouter:
    def db_for_read(self, model, **hints):
        if model._meta.model_name in ['centralmonitoramento', 'passagemplantao']:
            return 'plantao_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name in ['centralmonitoramento', 'passagemplantao']:
            return 'plantao_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in ['centralmonitoramento', 'passagemplantao']:
            return db == 'plantao_db'
        return None
