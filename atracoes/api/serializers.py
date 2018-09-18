from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracaoSerializer(ModelSerializer):
    criado_em = DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Atracao
        fields = ('id', 'descricao', 'horario_func', 'idede_minima', 'foto', 'criado_em')
