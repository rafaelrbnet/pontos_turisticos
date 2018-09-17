from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('localizacao', 'referencia', 'cidade', 'estado', 'pais')
