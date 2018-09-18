from rest_framework.fields import SerializerMethodField, DateTimeField
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    criado_em = DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto',
            'atracoes', 'comentarios', 'avaliacoes', 'enderecos',
            'descricao_completa', 'criado_em'
        )

    def get_descricao_completa(self, obj):
        return '{} - {}'.format(obj.nome, obj.descricao)


class CurrentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')
