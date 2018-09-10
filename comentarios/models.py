from django.db import models
from django.contrib.auth.models import User


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField('Comentario')
    aprovado = models.BooleanField('Aprovado?', default=False)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return self.usuario.first_name
