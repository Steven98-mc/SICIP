# Generated by Django 3.0.7 on 2020-09-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_canton', models.CharField(max_length=20)),
                ('cod_canton', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Conyuge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_conyuge', models.CharField(max_length=25)),
                ('apellido_conyuge', models.CharField(max_length=25)),
                ('cedula_connyugue', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_parroquia', models.CharField(max_length=20)),
                ('cod_parroquia', models.CharField(max_length=20)),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.Canton')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_tec', models.CharField(max_length=20)),
                ('apellidos_tec', models.CharField(max_length=20)),
                ('puesto_tec', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=100)),
                ('canton', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Canton')),
            ],
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_tramite', models.CharField(choices=[('0', 'Adjudicacion Individual'), ('1', 'Adjudicacion Colectiva'), ('2', 'Actualizacion catastral'), ('3', 'Levantamiento Predial'), ('4', 'Otros')], max_length=2)),
                ('numero', models.CharField(max_length=20)),
                ('fecha_reunion_ingreso', models.DateField()),
                ('fecha_reunion_sector', models.DateField()),
                ('viavilidad', models.CharField(choices=[('0', 'SI'), ('1', 'NO')], max_length=1)),
                ('escritura', models.BooleanField(blank=True)),
                ('plano', models.BooleanField(blank=True)),
                ('irm', models.BooleanField(blank=True)),
                ('copia_cedula', models.BooleanField(blank=True)),
                ('otro', models.CharField(blank=True, max_length=50)),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.Parroquia')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tecnico')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.Ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='stra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inspeccion', models.DateField()),
                ('fecha_certificado_mae', models.DateField()),
                ('fecha_ingreso_stra', models.DateField()),
                ('fecha_entrega_providencia', models.DateField()),
                ('numero_providencia', models.CharField(max_length=10)),
                ('registro_stra', models.CharField(max_length=20)),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='predio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField()),
                ('coordenadaX', models.CharField(max_length=50)),
                ('coordenadaY', models.CharField(max_length=50)),
                ('superficie', models.CharField(max_length=50)),
                ('geocodigo', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=1000)),
                ('tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='mdmqUrbana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso_dmq', models.DateField()),
                ('fecha_solicitud_cambio', models.DateField()),
                ('fecha_reingreso_dmq', models.DateField()),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.Tecnico')),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='mdmq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado_estado', models.CharField(max_length=20)),
                ('fecha_entrega_certificado_estado', models.DateField()),
                ('fecha_ingreso_registro_propiedad', models.DateField()),
                ('numero_registro', models.CharField(max_length=20)),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='InformeSociologica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reunion_soci', models.DateField()),
                ('homogenidad_predial', models.CharField(max_length=1000)),
                ('datos_predios', models.CharField(max_length=1000)),
                ('def_procesos_intervencion', models.CharField(max_length=1000)),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='InformeSectorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reunion_sec', models.DateField()),
                ('fecha_toma_puntos', models.DateField()),
                ('numero', models.CharField(max_length=10)),
                ('CoordenadaX', models.CharField(max_length=100)),
                ('CoordenadaY', models.CharField(max_length=100)),
                ('pdo_arranque', models.CharField(max_length=13)),
                ('numero_beneficiarios', models.CharField(max_length=13)),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.Tecnico')),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='InformeDirectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega_informacion', models.DateField()),
                ('fecha_firma_convenio', models.DateField()),
                ('numero_beneficiario_sector', models.CharField(max_length=20)),
                ('problemas_encontrados', models.CharField(max_length=1000)),
                ('posibles_soluciones', models.CharField(max_length=1000)),
                ('conf_socialpredio', models.CharField(max_length=1000)),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='gadpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega_plano_borrador', models.DateField()),
                ('fecha_firma_plano_original', models.DateField()),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vuelo', models.DateField()),
                ('topografia', models.CharField(max_length=100)),
                ('resolucion_gsd', models.CharField(max_length=100)),
                ('altura_vuelo', models.CharField(max_length=50)),
                ('velocidad_vuelo', models.CharField(max_length=50)),
                ('angulo_inclinacion', models.CharField(max_length=50)),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.Tecnico')),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('cedula', models.CharField(max_length=13)),
                ('celular', models.CharField(max_length=25)),
                ('correo', models.EmailField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=2)),
                ('dignidad', models.CharField(max_length=30)),
                ('edad', models.CharField(max_length=3)),
                ('estado_civil', models.CharField(choices=[('0', 'Soltero'), ('1', 'Casado'), ('2', 'Divorciado'), ('3', 'Viudo'), ('4', 'Union Libre')], default='0', max_length=5)),
                ('conyuge', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.Conyuge')),
                ('tramite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('razones', models.CharField(max_length=1000)),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.Tecnico')),
                ('tramite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.Tramite')),
            ],
        ),
    ]
