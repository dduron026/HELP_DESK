from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
	cliente = models.AutoField(db_column='CodCliente', primary_key=True)
	nombre = models.CharField(db_column='NombreCliente', max_length=200, blank=True, null=True)

	class Meta:
		db_table = 'Clientes'

	def __unicode__(self):
		return self.nombre

class Proyecto(models.Model):
	codProyecto = models.AutoField(db_column='CodProyecto', primary_key=True)
	nombre = models.CharField(db_column='NombreProyecto', max_length=200, blank=True, null=True)
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')

	class Meta:
		db_table = 'Proyectos'

	def __unicode__(self):
		return self.nombre


class Estados(models.Model):
	descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)

	class Meta:
		db_table = 'Estados'

	
	def __unicode__(self):
		return self.descripcion


class Personas(models.Model):
	nombre = models.CharField(db_column='NombrePersona', max_length=200, blank=True, null=True)
	codTipoPersona = models.ForeignKey('TipoPersonas', db_column='CodTipoPersona')
	codUsuario = models.ForeignKey(User, db_column='CodUsuario')

	class Meta:
		db_table = 'Personas'

	def __unicode__(self):
		return self.nombre

class TipoPersonas(models.Model):
	descripcion = models.CharField(db_column='DecripcionTipoPersona', max_length=200, blank=True, null=True)

	class Meta:
		db_table = 'TipoPersonas'

	def __unicode__(self):
		return self.descripcion	

class EncargadoClientes(models.Model):
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')
	codUsuario = models.ForeignKey(User, db_column='CodUsuario')

	class Meta:
		db_table = 'EncargadoClientes'

	

class Tickets(models.Model):
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')
	codProyecto = models.ForeignKey('Proyecto', db_column='CodProyecto')
	codEncargadoCliente = models.ForeignKey('EncargadoClientes', db_column='CodEncargadoCliente')
	codEstado = models.ForeignKey('Estados', db_column='CodEstado')
	comentario = models.TextField(max_length=500)
	usuarioCreador = models.CharField(db_column='UsuarioCreador', max_length=200, blank=True, null=True)
	UsuarioModificador = models.CharField(db_column='UsuarioModificador', max_length=200, blank=True, null=True)
	fechaCreacion = models.DateTimeField(db_column='FechaCreacion')
	fechaModificacion = models.DateTimeField(db_column='FechaModificacion')
	titulo = models.CharField(db_column='TituloTicket', max_length=200, blank=True, null=True)

	class Meta:
		db_table = 'Tickets'

	def __unicode__(self):
		return self.usuarioCreador

class DetalleTickets(models.Model):
	codTicket = models.ForeignKey('Tickets', db_column='CodTicket')
	CHOICES = (
		('A', 'ALTA'),
		('M', 'MEDIA'),
		('B', 'BAJA'),
		)
	prioridad = models.CharField(max_length=10, choices=CHOICES)
	archivo = models.FileField(db_column='Archivo')
	descripcion = models.CharField(db_column='DescripcionTicket', max_length=100, blank=True, null=True)
	estadoDetalleTickets = models.CharField(db_column='EstadoDetalleTickets', max_length=100, blank=True, null=True)
	asignadoA = models.ForeignKey('Personas', db_column='AsignadoA', blank=True, null=True)

	class Meta:
		db_table = 'DetalleTickets'