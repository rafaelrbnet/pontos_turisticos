from rest_framework.fields import SerializerMethodField, DateTimeField
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco
from core.models import PontoTuristico, DocIdentificacao
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    doc_identificacao = DocIdentificacaoSerializer()
    descricao_completa = SerializerMethodField(read_only=True)
    criado_em = DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto',
            'atracoes', 'comentarios', 'avaliacoes', 'enderecos', 'doc_identificacao',
            'descricao_completa', 'criado_em'
        )

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def cria_comentarios(self, comentarios, ponto):
        for comentario in comentarios:
            co = Comentario.objects.create(**comentario)
            ponto.comentarios.add(co)

    def cria_avaliacoes(self, avaliacoes, ponto):
        for avaliacao in avaliacoes:
            av = Avaliacao.objects.create(**avaliacao)
            ponto.avaliacoes.add(av)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        enderecos = validated_data['enderecos']
        comentarios = validated_data['comentarios']
        avaliacoes = validated_data['avaliacoes']
        doc = validated_data['doc_identificacao']
        del validated_data['atracoes']
        del validated_data['enderecos']
        del validated_data['comentarios']
        del validated_data['avaliacoes']
        del validated_data['doc_identificacao']

        ponto = PontoTuristico.objects.create(**validated_data)

        self.cria_atracoes(atracoes, ponto)
        self.cria_comentarios(comentarios, ponto)
        self.cria_avaliacoes(avaliacoes, ponto)

        end = Endereco.objects.create(**enderecos)
        ponto.enderecos = end

        doci = DocIdentificacao.objects.create(**doc)
        ponto.doc_identificacao = doci

        ponto.save()
        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)


class CurrentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')
