from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    criado_em = DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'aprovado', 'criado_em')
