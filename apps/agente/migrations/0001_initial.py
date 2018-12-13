# Generated by Django 2.1.3 on 2018-12-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('idAgente', models.AutoField(primary_key=True, serialize=False)),
                ('NroDocumento', models.CharField(max_length=7, unique=True)),
                ('Apellido', models.CharField(max_length=30)),
                ('Nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Agentes',
                'verbose_name': 'Agente',
            },
        ),
    ]
