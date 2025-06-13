from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Sensor,Ambiente,Historico,Usuario

# Serializa(transforma em JSON) todos os campos(fields) do modelo(model) Sensor
class SensoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensor
        fields = '__all__'


    # cria uma representação dos dados para depois serem usados para gerar um excel    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
    
# Serializa(transforma em JSON) todos os campos(fields) do modelo(model) ambiente
class AmbientesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ambiente
        fields = '__all__'


    # cria uma representação dos dados para depois serem usados para gerar um excel    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
    
# Serializa(transforma em JSON) todos os campos(fields) do modelo(model) Historico
class HistoricoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Historico
        fields = '__all__'


    # cria uma representação dos dados para depois serem usados para gerar um excel    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class LoginSerializer(TokenObtainPairSerializer):
    
    # valida o campo customizado do modelo de abstractUser "categoria", para receber o valor da categoria enviada na requisição
    def validate(self, attrs):
        data = super().validate(attrs)
        data['usuario'] = {
            'categoria': self.user.categoria
        }
        return data


class CadastroSerializer(serializers.ModelSerializer):
    
    # Cria dois campos password (um normal e outro confirme sua senha)
    password = serializers.CharField(write_only=True,required=True,style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True,required=True,style={'input_type': 'password'})

    # Usa o modelo usuario com os campos username(do abstractUser) os customizados categoria(do model), password e password2 criados acima
    class Meta:
        model = Usuario
        fields = ('username','password','password2','categoria')
        
    
    # Valida se as senhas enviadas batem
    def validate(self,attrs):
        data = super().validate(attrs)
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password':'As senhas não batem'}
            )
        return attrs
    
    # Cria na requisição um usuario com os campos validados anteriormente e inserindo as senhas tambem validadas no modelo
    def create(self, validated_data):
        user = Usuario.objects.create(
            username= validated_data['username'],
            categoria=validated_data['categoria'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user