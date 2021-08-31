from rest_framework.response import Response
from rest_framework.views import APIView  #
from apps.users.models import User  #
from apps.users.api.serializers import UserSerializers  #

"""
Este archivo servira para poner los metodos relacionados con las vistas urls, sera para poner los metodos que devolveran
los datos de la api.
"""


class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()  # Se obtiene todos los datos de la BBDD
        """
        Se serializa lo obtenido. Con 'many' se indica que hay que serializar todos los elementos a JSON, si esto no 
        estubiera solo serviria para un solo objeto.        """
        users_serializer = UserSerializers(users, many=True)
        # Aqui se devuelve los datos serializados o convertidos a JSON usando la el '.data'
        return Response(users_serializer.data)
