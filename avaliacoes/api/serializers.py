from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    criado_em = DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Avaliacao
        fields = ('id', 'usuario', 'comentario', 'nota', 'criado_em')
