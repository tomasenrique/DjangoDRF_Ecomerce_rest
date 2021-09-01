from django.urls import path
# from apps.users.api.api import UserAPIView  # Aqui se esta importando la clase que sirve como ruta para el JSON
from apps.users.api.api import user_api_view  # Metodo con decorador para el JSON
from apps.users.api.api import user_detail_view  # Metodo para realizar la actualizacion

"""
Este archivo servira para poner las rutas urls que estan enlazadas con el archivo urls.py del proyecto principal
"""

urlpatterns = [
    # path('usuario/', UserAPIView.as_view(), name='usuario_api'),
    path('usuario/', user_api_view, name='usuario_api'),  # Metodo con decorador para la ruta
    path('usuario/<int:pk>/', user_detail_view, name='usuario_detail_api_view'),  # Metodo con parametro
]
