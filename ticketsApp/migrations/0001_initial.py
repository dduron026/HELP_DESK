# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 14:44
from __future__ import unicode_literals

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, db_column=b'NombreCliente', max_length=200, null=True)),
            ],
            options={
                'db_table': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='DetalleTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridad', models.CharField(max_length=10)),
                ('archivo', models.FileField(db_column=b'Archivo', upload_to=b'')),
                ('descripcion', models.CharField(blank=True, db_column=b'DescripcionTicket', max_length=100, null=True)),
                ('estadoDetalleTickets', models.CharField(blank=True, db_column=b'EstadoDetalleTickets', max_length=100, null=True)),
            ],
            options={
                'db_table': 'DetalleTickets',
            },
        ),
        migrations.CreateModel(
            name='EncargadoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(db_column=b'CodCliente', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Cliente')),
                ('codUsuario', models.ForeignKey(db_column=b'CodUsuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'EncargadoClientes',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, db_column=b'Descripcion', max_length=200, null=True)),
            ],
            options={
                'db_table': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, db_column=b'NombrePersona', max_length=200, null=True)),
            ],
            options={
                'db_table': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, db_column=b'NombreProyecto', max_length=200, null=True)),
                ('cliente', models.ForeignKey(db_column=b'CodCliente', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Cliente')),
            ],
            options={
                'db_table': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=500)),
                ('usuarioCreador', models.CharField(blank=True, db_column=b'UsuarioCreador', max_length=200, null=True)),
                ('UsuarioModificador', models.CharField(blank=True, db_column=b'UsuarioModificador', max_length=200, null=True)),
                ('fechaCreacion', models.DateTimeField(db_column=b'FechaCreacion')),
                ('fechaModificacion', models.DateTimeField(db_column=b'FechaModificacion')),
                ('titulo', models.CharField(blank=True, db_column=b'TituloTicket', max_length=200, null=True)),
                ('cliente', models.ForeignKey(db_column=b'CodCliente', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Cliente')),
                ('codEncargadoCliente', models.ForeignKey(db_column=b'CodEncargadoCliente', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.EncargadoCliente')),
                ('codEstado', models.ForeignKey(db_column=b'CodEstado', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Estado')),
                ('codProyecto', models.ForeignKey(db_column=b'CodProyecto', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Proyecto')),
            ],
            options={
                'db_table': 'Tickets',
            },
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, db_column=b'DecripcionTipoPersona', max_length=200, null=True)),
            ],
            options={
                'db_table': 'TipoPersonas',
            },
        ),
        migrations.AddField(
            model_name='persona',
            name='codTipoPersona',
            field=models.ForeignKey(db_column=b'CodTipoPersona', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.TipoPersona'),
        ),
        migrations.AddField(
            model_name='persona',
            name='codUsuario',
            field=models.ForeignKey(db_column=b'CodUsuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='detalleticket',
            name='asignadoA',
            field=models.ForeignKey(blank=True, db_column=b'AsignadoA', null=True, on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Persona'),
        ),
        migrations.AddField(
            model_name='detalleticket',
            name='codTicket',
            field=models.ForeignKey(db_column=b'CodTicket', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Ticket'),
        ),
    ]
