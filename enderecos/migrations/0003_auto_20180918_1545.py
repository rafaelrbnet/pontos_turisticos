# Generated by Django 2.1.1 on 2018-09-18 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0002_auto_20180911_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='atualizado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Atualizado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
    ]
