# Generated by Django 4.2.2 on 2023-07-26 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('MATUTINO', 'MATUTITO'), ('TARDE', 'TARDE'), ('FIN DE SEMANA', 'FIN DE SEMANA')], default='MATUTITO', max_length=40)),
                ('nombre_seccion', models.CharField(max_length=30)),
                ('cupor_por_seccion', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dui_docente', models.CharField(default='', max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('nip_docente', models.CharField(max_length=20, null=True)),
                ('alumnos_a_cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_alumnos.alumno')),
                ('seccion_cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_docentes.secciones')),
            ],
        ),
    ]