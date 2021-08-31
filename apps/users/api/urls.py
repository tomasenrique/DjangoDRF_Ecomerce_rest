from django.urls import path
from apps.users.api.api import UserAPIView

"""
Este archivo servira para poner las rutas urls que estan enlazadas con el archivo urls.py del proyecto principal
"""

urlpatterns = [
    path('usuario/', UserAPIView.as_view(), name='usuario_api'),
]
