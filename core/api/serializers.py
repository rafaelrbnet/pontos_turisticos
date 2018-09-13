from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto')


class CurrentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')
