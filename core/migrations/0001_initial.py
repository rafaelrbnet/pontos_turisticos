# Generated by Django 2.1.1 on 2018-09-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('aprovado', models.BooleanField(default=False, verbose_name='Aprovado?')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
            ],
        ),
    ]
