# Generated by Django 2.1.3 on 2018-12-11 03:54

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
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('SectorEconomico', models.CharField(choices=[(1, 'Profesional Independiente'), (2, 'Comerciante'), (3, 'Industrial'), (4, 'Agropecuario'), (5, 'Empleado Asalariado'), (6, 'Otro')], max_length=1)),
                ('TipoPersona', models.CharField(choices=[(1, 'Fisica'), (2, 'Juridica')], max_length=1)),
                ('PaisDoc', models.CharField(choices=[('PY', 'Paraguay'), ('BR', 'Brasil')], max_length=2)),
                ('TipoDocumento', models.CharField(choices=[(1, 'Documento Indentidad'), (2, 'CRC Codigo Persona no Residente'), (3, 'CRP Codigo de Persona Residente Permanente'), (4, 'RUC'), (5, 'Pasaporte')], max_length=1)),
                ('NumeroDocumento', models.CharField(max_length=10)),
                ('Apellido', models.CharField(max_length=30)),
                ('Nombre', models.CharField(max_length=30)),
                ('NombreCompleto', models.CharField(max_length=60)),
                ('FechaNacimiento', models.DateField()),
                ('Genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('EstadoCivil', models.CharField(choices=[(1, 'Casado'), (2, 'Soltero'), (3, 'Concubinato'), (4, 'Divorciado'), (5, 'Viudo'), (6, 'Sin datos')], max_length=1)),
                ('Nacionalidad', models.CharField(choices=[('PY', 'Paraguayo'), ('BR', 'Brasilero')], max_length=1)),
                ('Telefono', models.CharField(max_length=10)),
                ('TipoDireccion', models.CharField(choices=[(1, 'Residencia'), (2, 'Laboral'), (3, 'Comercial'), (4, 'Fiscal')], max_length=1)),
                ('Pais', models.CharField(choices=[('PY', 'Paraguay'), ('BR', 'Brasil')], max_length=2)),
                ('Departamento', models.CharField(choices=[('ASU', 'Asuncíon'), ('1', 'Concepción'), ('2', 'San Pedro'), ('3', 'Cordillera'), ('4', 'Guairá'), ('5', 'Caaguazú'), ('6', 'Caazapá'), ('7', 'Itapúa'), ('8', 'Misiones'), ('9', 'Paraguarí'), ('10', 'Alto Paraná'), ('11', 'Central Areguá'), ('12', 'Ñeembucú'), ('13', 'Amambay'), ('14', 'Canindeyú'), ('15', 'Presidente Hayes'), ('16', 'Boquerón'), ('17', 'Alto Paraguay')], max_length=3)),
                ('Ciudad', models.CharField(max_length=30)),
                ('Bario', models.CharField(max_length=30)),
                ('DireccionLibre', models.CharField(max_length=255)),
                ('ComprobanteIngreso', models.CharField(max_length=30)),
                ('Salario', models.CharField(max_length=10)),
                ('CargoTrabajo', models.CharField(max_length=30)),
                ('Dependiente', models.CharField(choices=[(1, 'NO'), (2, 'SI')], max_length=1)),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]