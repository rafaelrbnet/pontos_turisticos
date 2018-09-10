from django.db import models


class PontoTuristico(models.Model):
    nome = models.CharField('Nome', max_length=150)
    descricao = models.TextField('Descrição')
    aprovado = models.BooleanField('Aprovado?', default=False)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return self.nome
