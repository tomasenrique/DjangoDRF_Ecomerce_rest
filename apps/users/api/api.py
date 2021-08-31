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
        # Para realizar una validación de datos y ver si coincide los datos recibidos con el modelo del sistema
        user_serialiser = UserSerializers(data=request.data)
        if user_serialiser.is_valid():  # Para verificar su los datos son validos
            user_serialiser.save()  # Guarda los datos en la BBDD
            return Response(user_serialiser.data)  #
        return Response(user_serialiser.errors)  # Para mostrar mensaje de error si no pasa la validación
