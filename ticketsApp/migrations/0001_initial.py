# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-24 00:56
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
                ('nombre_cliente', models.CharField(blank=True, db_column=b'NombreCliente', max_length=200, null=True)),
                ('correo_cliente', models.EmailField(blank=True, db_column=b'CorreoCliente', max_length=254, null=True)),
                ('usuario', models.ForeignKey(blank=True, db_column=b'Usuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Clientes',
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
                ('descripcion_estado', models.CharField(blank=True, db_column=b'DescripcionEstado', max_length=200, null=True)),
            ],
            options={
                'db_table': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(blank=True, db_column=b'NombreProyecto', max_length=200, null=True)),
                ('cliente', models.ForeignKey(db_column=b'CodCliente', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Cliente')),
                ('codUsuario', models.ForeignKey(db_column=b'CodUsuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True, max_length=500, null=True)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, db_column=b'FechaCreacion')),
                ('fechaModificacion', models.DateTimeField(auto_now=True, db_column=b'FechaModificacion')),
                ('titulo', models.CharField(db_column=b'TituloTicket', max_length=200)),
                ('prioridad', models.CharField(db_column=b'Prioridad', max_length=20)),
                ('archivo', models.FileField(blank=True, db_column=b'Archivo', null=True, upload_to=b'uploads/')),
                ('descripcion_ticket', models.CharField(db_column=b'DescripcionTicket', max_length=500)),
                ('Proyecto', models.ForeignKey(db_column=b'CodProyecto', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Proyecto')),
                ('UsuarioModificador', models.ForeignKey(db_column=b'UsuarioModificador', on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioModificador', to=settings.AUTH_USER_MODEL)),
                ('asignadoA', models.ForeignKey(blank=True, db_column=b'AsignadoA', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cliente', models.ForeignKey(db_column=b'CodCliente', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Cliente')),
                ('codEncargadoCliente', models.ForeignKey(db_column=b'CodEncargadoCliente', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.EncargadoCliente')),
                ('codEstado', models.ForeignKey(db_column=b'CodEstado', on_delete=django.db.models.deletion.CASCADE, to='ticketsApp.Estado')),
                ('usuarioCreador', models.ForeignKey(db_column=b'UsuarioCreador', on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioCreador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Tickets',
            },
        ),
    ]
