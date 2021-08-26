from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'  # Cambiada la ruta para ubicar la aplicacion, se hacer por cada una.
