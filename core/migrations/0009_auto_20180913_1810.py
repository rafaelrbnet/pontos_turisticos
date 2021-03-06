# Generated by Django 2.1.1 on 2018-09-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180911_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(blank=True, related_name='pontos_turisticos', to='avaliacoes.Avaliacao', verbose_name='Avaliações'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(blank=True, related_name='pontos_turisticos', to='comentarios.Comentario', verbose_name='Comentários'),
        ),
    ]
