from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth.models import User
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer, CurrentUserSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'enderecos__localizacao')
    # lookup_field = 'nome' estes tipo de campo deve ser conswiderado como unique. ex CPF
    permission_classes = (DjangoModelPermissions,) # herança do modulo de permissão do admin
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = PontoTuristico.objects.filter(nome__iexact=nome)

        if descricao:
            queryset = PontoTuristico.objects.filter(descricao__iexact=descricao)

        return queryset

    @action(methods=['get'], detail=True)
    def denunciar(self, request, *args, **kwargs):
        return Response({'Action Padrão': kwargs})

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=pk)
        ponto.atracoes.set(atracoes)
        ponto.save()

        return HttpResponse('Atrações associadas com sucesso')

    # @todo Fazer as demais actions para: comentarios, avaliacoes, enderecos, doc_identificacao


class CurrentUserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('first_name', 'last_name', 'username', 'email')
    lookup_field = 'username'
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
