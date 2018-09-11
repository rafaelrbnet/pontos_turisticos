from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao


class PontoTuristico(models.Model):
    nome = models.CharField('Nome', max_length=150)
    descricao = models.TextField('Descrição')
    aprovado = models.BooleanField('Aprovado?', default=False)
    atracoes = models.ManyToManyField(
        Atracao, verbose_name='Atrações', related_name='pontos_turisticos'
    )
    comentarios = models.ManyToManyField(
        Comentario, verbose_name='Comentários', related_name='pontos_turisticos'
    )
    avaliacoes = models.ManyToManyField(
        Avaliacao, verbose_name='Avaliações', related_name='pontos_turisticos'
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return self.nome
