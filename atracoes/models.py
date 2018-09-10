from django.db import models


class Atracao(models.Model):
    nome = models.CharField('Nome', max_length=150)
    descricao = models.TextField('Descrição')
    horario_func = models.TextField('Horário de Funcionamento')
    idede_minima = models.IntegerField('Idade Minima')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return self.nome
