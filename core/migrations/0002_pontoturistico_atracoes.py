# Generated by Django 2.1.1 on 2018-09-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(related_name='atraco', to='atracoes.Atracao', verbose_name='Atrações'),
        ),
    ]
