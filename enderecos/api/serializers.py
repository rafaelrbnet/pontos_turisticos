from rest_framework.fields import DateTimeField, SerializerMethodField
from rest_framework.serializers import ModelSerializer
from django.utils.timesince import timesince
from enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    criado_em = DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    atualizado_em = SerializerMethodField()

    class Meta:
        model = Endereco
        fields = (
            'id', 'localizacao', 'referencia', 'cidade', 'estado', 'pais', 'latitude', 'longitude', 'criado_em',
            'atualizado_em'
        )

    def get_atualizado_em(self, obj):
        return timesince(obj.atualizado_em)
