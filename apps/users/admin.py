from django.contrib import admin

from apps.users.models import User

# Se registra la vista para poder gestionarlo en el panel de administración
admin.site.register(User)
