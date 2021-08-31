from rest_framework.response import Response
# from rest_framework.views import APIView  #
from apps.users.models import User  #
from apps.users.api.serializers import UserSerializers  #
from rest_framework.decorators import api_view  # Para usar decorador en las funciones

"""
Este archivo servira para poner los metodos relacionados con las vistas urls, sera para poner los metodos que devolveran
los datos de la api.
"""


# class UserAPIView(APIView):
#     def get(self, request):
#         users = User.objects.all()  # Se obtiene todos los datos de la BBDD
#         """
#         Se serializa lo obtenido. Con 'many' se indica que hay que serializar todos los elementos a JSON, si esto no
#         estubiera solo serviria para un solo objeto.        """
#         users_serializer = UserSerializers(users, many=True)
#         # Aqui se devuelve los datos serializados o convertidos a JSON usando la el '.data'
#         return Response(users_serializer.data)


# Este decorador sirve para indicar los metodos http permiten la función y van en una lista
@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()  # Se obtiene todos los datos de la BBDD
        users_serializer = UserSerializers(users, many=True)
        # Aqui se devuelve los datos serializados o convertidos a JSON usando la el '.data'
        return Response(users_serializer.data)

    elif request.method == 'POST':
        print(request.data)  # Para probar que los datos llegan al servidor, ver en la consola
