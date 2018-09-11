from django.contrib.auth.models import User
from django.db import models


class Avaliacao(models.Model):
    usuario = models.ForeignKey(
        User, verbose_name='Avaliações', related_name='avaliacoes', on_delete=models.CASCADE,
    )
    comentario = models.TextField('Comentário',null=True, blank=True)
    NOTAS = (
        (0, 'Neutra'),
        (1, 'Ruim'),
        (2, 'Boa'),
        (3, 'Ótimo'),
    )
    nota = models.IntegerField('Nota', choices=NOTAS, default=0, blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return str(self.nota)