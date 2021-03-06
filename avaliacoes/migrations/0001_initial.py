# Generated by Django 2.1.1 on 2018-09-11 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentário')),
                ('nota', models.IntegerField(blank=True, choices=[(0, 'Ruim'), (1, 'Bom'), (2, 'Ótimo')], default=0, verbose_name='Nota')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to=settings.AUTH_USER_MODEL, verbose_name='Avaliações')),
            ],
        ),
    ]
