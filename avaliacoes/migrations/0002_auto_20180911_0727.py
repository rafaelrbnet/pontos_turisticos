# Generated by Django 2.1.1 on 2018-09-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.IntegerField(blank=True, choices=[(0, 'Neutra'), (1, 'Ruim'), (2, 'Boa'), (3, 'Ótimo')], default=0, verbose_name='Nota'),
        ),
    ]