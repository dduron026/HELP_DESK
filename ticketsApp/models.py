from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
	nombre_cliente = models.CharField(db_column='NombreCliente', max_length=200, blank=True, null=True)
	correo_cliente = models.EmailField(db_column='CorreoCliente', blank=True, null=True)

	class Meta:
		db_table = 'Clientes'

	def __unicode__(self):
		return self.nombre

class Proyecto(models.Model):
	nombre_proyecto = models.CharField(db_column='NombreProyecto', max_length=200, blank=True, null=True)
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')

	class Meta:
		db_table = 'Proyectos'

	def __unicode__(self):
		return self.nombre


class Estado(models.Model):
	descripcion_estado = models.CharField(db_column='DescripcionEstado', max_length=200, blank=True, null=True)

	class Meta:
		db_table = 'Estados'

	
	def __unicode__(self):
		return self.descripcion


class Persona(models.Model):
	nombre_persona = models.CharField(db_column='NombrePersona', max_length=200, blank=True, null=True)
	codTipoPersona = models.ForeignKey('TipoPersona', db_column='CodTipoPersona')
	codUsuario = models.ForeignKey(User, db_column='CodUsuario')

	class Meta:
		db_table = 'Personas'

	def __unicode__(self):
		return self.nombre

class TipoPersona(models.Model):
	descripcion_tipoPersona = models.CharField(db_column='DecripcionTipoPersona', max_length=200, blank=True, null=True)

	class Meta:
		db_table = 'TipoPersonas'

	def __unicode__(self):
		return self.descripcion	

class EncargadoCliente(models.Model):
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')
	codUsuario = models.ForeignKey(User, db_column='CodUsuario')

	class Meta:
		db_table = 'EncargadoClientes'

	

class Ticket(models.Model):
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')
	codProyecto = models.ForeignKey('Proyecto', db_column='CodProyecto')
	codEncargadoCliente = models.ForeignKey('EncargadoCliente', db_column='CodEncargadoCliente')
	codEstado = models.ForeignKey('Estado', db_column='CodEstado')
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

class DetalleTicket(models.Model):
	codTicket = models.ForeignKey('Ticket', db_column='CodTicket')
	prioridad = models.CharField(max_length=10)
	archivo = models.FileField(db_column='Archivo')
	descripcion_ticket = models.CharField(db_column='DescripcionTicket', max_length=100, blank=True, null=True)
	estadoDetalleTickets = models.CharField(db_column='EstadoDetalleTickets', max_length=100, blank=True, null=True)
	asignadoA = models.ForeignKey('Persona', db_column='AsignadoA', blank=True, null=True)

	class Meta:
		db_table = 'DetalleTickets'