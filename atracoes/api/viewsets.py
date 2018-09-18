from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('id', 'descricao', 'idede_minima')
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
