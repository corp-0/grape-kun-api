from rest_framework import status
from rest_framework.generics import RetrieveAPIView, GenericAPIView,UpdateAPIView
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UsuarioSerializer, RegistrarUsuarioSerializer, LoginUsuarioSerializer, ActualizarUsuarioSerializer
from .models import Usuario
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied

class UsuarioView(RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LoginConCredsView(GenericAPIView):
    serializer_class = LoginUsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UsuarioSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        }, status=status.HTTP_200_OK)

class RegistrarUsuarioView(GenericAPIView):
    serializer_class = RegistrarUsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UsuarioSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        }, status=status.HTTP_200_OK)

class ActualizarUsuarioView(GenericAPIView):
    serializer_class = ActualizarUsuarioSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(pk=request.user.pk)
            if request.user != usuario:
                raise PermissionDenied
        except Usuario.DoesNotExist:
            return Response({"error": "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied:
            return Response({"error": "No tiene permisos para realizar esta acción"}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(usuario, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        respueta = {"resultado": "Usuario actualizado correctamente", **serializer.data}
        return Response(respueta, status=status.HTTP_200_OK)

