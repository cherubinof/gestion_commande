from django.apps import AppConfig


class AppProduitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_produit'
    
    
    
    
    def ready(self):
        import app_produit.signals

