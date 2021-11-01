from rest_framework import serializers
from django.contrib.auth import authenticate
from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    favoritos = serializers.JSONField()
    preferencias = serializers.JSONField()

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'fec_nac', 'preferencias', 'favoritos')

class RegistrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'password', 'fec_nac')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = Usuario.objects.create_user(validated_data['username'],
                                               validated_data['email'],
                                               validated_data['password'])
            return user

class LoginUsuarioSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        user = authenticate(username=attrs['email'], password=attrs['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Credenciales inválidas')