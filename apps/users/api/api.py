from rest_framework.response import Response
# from rest_framework.views import APIView  #
from apps.users.models import User  #
from apps.users.api.serializers import UserSerializers  #
from rest_framework.decorators import api_view  # Para usar decorador en las funciones
from rest_framework import status  # para usar las respuestas de estado en la api

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
    # GET LIST
    if request.method == 'GET':  # Para listar todos los registros de las BBDD
        users = User.objects.all()  # Se obtiene todos los datos de la BBDD
        users_serializer = UserSerializers(users, many=True)
        # Aqui se devuelve los datos serializados o convertidos a JSON usando la el '.data'
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    # POST CREATE
    elif request.method == 'POST':  # Para agregar un registros a la BBDD
        # Para realizar una validación de datos y ver si coincide los datos recibidos con el modelo del sistema
        user_serialiser = UserSerializers(data=request.data)
        if user_serialiser.is_valid():  # Para verificar su los datos son validos
            user_serialiser.save()  # Guarda los datos en la BBDD
            return Response({'Message': "Registro de usuario agregado."}, status=status.HTTP_201_CREATED)

        # Para mostrar mensaje de error si no pasa la validación
        return Response(user_serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):
    user = User.objects.filter(id=pk).first()  # obteniendo registro po id (consulta)

    # VALIDATION
    if user:  # verifica si existe o no
        # RETRIEVE
        if request.method == 'GET':  # Para listar todos los registros de las BBDD
            user_serializer = UserSerializers(user)  # serializando objeto
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        # UPDATE
        elif request.method == 'PUT':  # Para actualizar un registro
            user_serializer = UserSerializers(user, data=request.data)

            # VALIDATION
            if user_serializer.is_valid():  # Para verificar su los datos son validos
                user_serializer.save()  # Guarda los datos en la BBDD actualizados
                return Response(user_serializer.data, status=status.HTTP_200_OK)  #
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # DELETE
        elif request.method == 'DELETE':  # Para eliminar un registro
            user.delete()
            return Response({'Message': "Registro eliminado correctamente."}, status=status.HTTP_200_OK)
    return Response({'Message': "No se ha encontrado usuario con estos datos."}, status=status.HTTP_400_BAD_REQUEST)
