from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'localizacao', 'referencia', 'cidade', 'estado', 'pais', 'latitude', 'longitude')
