from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Sensor,Ambiente,Historico,Usuario

class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)

        return data
class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'
class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['usuario'] = {
            'categoria': self.user.categoria
        }
        return data
class CadastroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True,required=True,style={'input_type': 'password'})

    class Meta:
        model = Usuario
        fields = ('username','password','password2','categoria')
    def validate(self,attrs):
        data = super().validate(attrs)
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password':'As senhas não batem'}
            )
        return attrs
    def create(self, validated_data):
        user = Usuario.objects.create(
            username= validated_data['username'],
            categoria=validated_data['categoria'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user