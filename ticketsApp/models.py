from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Cliente(models.Model):
	nombre_cliente = models.CharField(db_column='NombreCliente', max_length=200, blank=True, null=True)
	correo_cliente = models.EmailField(db_column='CorreoCliente', blank=True, null=True)
	usuario = models.ForeignKey(User,db_column='Usuario', blank=True, null=True)

	class Meta:
		db_table = 'Clientes'

	def __unicode__(self):
		return self.nombre_cliente

class Proyecto(models.Model):
	nombre_proyecto = models.CharField(db_column='NombreProyecto', max_length=200, blank=True, null=True)
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')
	codUsuario = models.ForeignKey(User, db_column='CodUsuario')


	class Meta:
		db_table = 'Proyectos'

	def __unicode__(self):
		return self.nombre_proyecto

class EncargadoCliente(models.Model):
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')
	codUsuario = models.ForeignKey(User, db_column='CodUsuario')

	class Meta:
		db_table = 'EncargadoClientes'



class Estado(models.Model):
	descripcion_estado = models.CharField(db_column='DescripcionEstado', max_length=200, blank=True, null=True)

	class Meta:
		db_table = 'Estados'

	
	def __unicode__(self):
		return self.descripcion_estado
	

class Ticket(models.Model):
	cliente = models.ForeignKey('Cliente', db_column='CodCliente')
	Proyecto = models.ForeignKey('Proyecto', db_column='CodProyecto')
	codEncargadoCliente = models.ForeignKey('EncargadoCliente', db_column='CodEncargadoCliente')
	codEstado = models.ForeignKey('Estado', db_column='CodEstado')
	comentario = models.TextField(max_length=500, blank=False)		
	usuarioCreador = models.ForeignKey(User, db_column='UsuarioCreador', related_name='UsuarioCreador')
	UsuarioModificador = models.ForeignKey(User,db_column='UsuarioModificador', related_name='UsuarioModificador')	
	fechaCreacion = models.DateTimeField(db_column='FechaCreacion', auto_now_add=True)
	fechaModificacion = models.DateTimeField(db_column='FechaModificacion', auto_now=True)
	titulo = models.CharField(db_column='TituloTicket', max_length=200, blank=True, null=True)
	prioridad = models.CharField(db_column='Prioridad', max_length=20)
	archivo = models.FileField(db_column='Archivo', upload_to='uploads/', null=True, blank=True)
	descripcion_ticket = models.CharField(db_column='DescripcionTicket', max_length=500, blank=True, null=True)
	asignadoA = models.ForeignKey(User, db_column='AsignadoA', blank=True, null=True)


	class Meta:
		db_table = 'Tickets'

	def __unicode__(self):
		return '%s %s' % (self.titulo, self.comentario)




