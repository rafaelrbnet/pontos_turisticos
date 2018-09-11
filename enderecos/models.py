from django.db import models


class Endereco(models.Model):
    localizacao = models.CharField('Localização', max_length=150)
    referencia = models.CharField('Referência', max_length=150, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    pais = models.CharField('País', max_length=50)
    latitude = models.DecimalField('Latitude', max_digits=20, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField('Longitude', max_digits=20, decimal_places=7, blank=True, null=True)

    def __str__(self):
        return self.localizacao
