from rest_framework import serializers
from apps.users.models import User

"""
Esta clase serializadora se encargara de convertir cualquier estructura del modelo 'User' a formato JSON y devolver lo
que le especifiquemos en la variable 'fields'
"""


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'  # Con esto se indica que queremos mostrar todos los campos del modelo.
        fields = ['username', 'email', 'name', 'last_name']  # Sise quiere se puede especificar determinados campos
