# Generated by Django 3.2.6 on 2023-04-13 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manejador_de_registros_de_historias_clinicas', '0006_auto_20230412_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia_clinica',
            name='fecha',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
