# Generated by Django 2.1.3 on 2018-12-11 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20181211_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Dependiente',
            field=models.PositiveSmallIntegerField(choices=[(1, 'NO'), (2, 'SI')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='EstadoCivil',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Casado'), (2, 'Soltero'), (3, 'Concubinato'), (4, 'Divorciado'), (5, 'Viudo'), (6, 'Sin datos')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='TipoDocumento',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Documento Indentidad'), (2, 'CRC Codigo Persona no Residente'), (3, 'CRP Codigo de Persona Residente Permanente'), (4, 'RUC'), (5, 'Pasaporte')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='TipoPersona',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Fisica'), (2, 'Juridica')]),
        ),
    ]
