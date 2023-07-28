# Generated by Django 4.2.2 on 2023-07-26 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_alumnos', '0001_initial'),
        ('app_docentes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='docente_encargado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_docentes.docente'),
        ),
    ]