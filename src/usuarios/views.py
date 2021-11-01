from django.core.exceptions import PermissionDenied
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer, RegistrarUsuarioSerializer, LoginUsuarioSerializer, \
    ActualizarUsuarioSerializer


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
    permission_classes = [IsAuthenticated]

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
        respuesta = {"resultado": "Usuario actualizado correctamente", **serializer.data}
        return Response(respuesta, status=status.HTTP_200_OK)


class LoginConTokenView(KnoxLoginView):
    def get_post_response_data(self, request, token, instance):
        UserSerializer = self.get_user_serializer_class()

        data = {
            'token': token
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data
        return data

    def get_user_serializer_class(self):
        return UsuarioSerializer
