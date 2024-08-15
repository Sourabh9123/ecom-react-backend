from django.apps import AppConfig


class CartappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cartapp'


    def ready(self):
        import cartapp.signals