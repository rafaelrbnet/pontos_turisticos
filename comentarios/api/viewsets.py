from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('usuario__username', 'comentario')
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
