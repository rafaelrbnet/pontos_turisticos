from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth.models import User
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer, CurrentUserSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})


class CurrentUserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer
