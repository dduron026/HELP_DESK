from django.shortcuts import render

# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ticketsApp.forms import *
from .models import * 
 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 


def user_unicode_patch(self): #PARA MOSTRAR EL NOMBRE Y APELLIDO DEL USUARIO
	return '%s %s' % (self.first_name, self.last_name)

User.__unicode__= user_unicode_patch


@login_required()
def ingreso_solicitud(request):
	
	formulario_ingreso = TicketForm()
	try:
		clientes = Cliente()
		
		encargado_cliente = EncargadoCliente.objects.get(codUsuario__pk=request.user.pk)
		formulario_ingreso.fields["codProyecto"] = forms.ModelChoiceField(queryset=Proyecto.objects.filter(cliente__pk=encargado_cliente.cliente.pk))

	except Exception as e:
		pass
	try:
		if request.POST:
			ticket = Ticket()
			proyecto = Proyecto()
			
			encargado = EncargadoCliente.objects.get(codUsuario=request.user)
			ticket.codProyecto = Proyecto.objects.get(pk=request.POST.get('codProyecto'))
			ticket.codEncargadoCliente = encargado
			ticket.cliente = Cliente.objects.get(pk=encargado.cliente.pk)
			ticket.codEstado = Estado.objects.get(pk=1)	
			ticket.titulo = None if request.POST.get('titulo') == '' else request.POST.get('titulo')

			ticket.descripcion_ticket = None if request.POST.get('descripcion_ticket') == '' else request.POST.get('descripcion_ticket')
			ticket.comentario = None if request.POST.get('comentario') == '' else request.POST.get('comentario')
			ticket.prioridad = None if request.POST.get('prioridad') == '' else request.POST.get('prioridad')		
			ticket.usuarioCreador = User.objects.get(id=request.user.pk)
			ticket.UsuarioModificador = request.user
			try:
				ticket.archivo = request.FILES['archivo']
			except Exception as e:
					pass	

			ticket.save()

			remitente = 'ticket.soporte@bi-dss.com'
			destinatario = "denisduron83@gmail.com"
					
			msg = MIMEMultipart()

			msg['From'] = remitente
			msg['To'] = destinatario
			# msg['To'] = ", ".join(destinatario) varios a la vez
			msg['Subject'] = '{0}{1}{2}{3}{4}{5}{6}'.format('TICKET #', ' ', ticket.pk,' ', 'de', ' ', ticket.codProyecto)

			body = 'Saludos <b>Denis</b>,<br> el usuario <b>{0}{1}{2}{3}</b> ha reportado el ticket # <b>[{4}]</b> con nivel de urgencia <b>{5}</b>.<br><b>[Prueba].<b>'.format(request.user.first_name, ' ', request.user.last_name, ' ',ticket.pk, ticket.prioridad ) 

			msg.attach(MIMEText(body.encode('utf-8'), 'html', 'utf-8'))	
			username = 'ticket.soporte@bi-dss.com'
			password = 'Ticket2017'		
			try:
				server = smtplib.SMTP('smtp.office365.com:587')
				server.starttls()
				server.login(username,password)
				server.sendmail(remitente, destinatario, msg.as_string())
				server.quit()
			except Exception as e:
				print e
	except Exception as e:
		pass
		
	print formulario_ingreso				

	ctx = {	
		'formulario_ingreso': formulario_ingreso,		
	}
	return render(request, 'nuevaSolicitud.html', ctx)



@login_required()
def listado_solicitudes(request):
	if request.user.is_superuser:
		lista = Ticket.objects.all().order_by('id')
	else:
		lista = Ticket.objects.filter(usuarioCreador=request.user)
	return render(request, 'ticket_listado.html', {'lista':lista})


@login_required()
def ticket_editar(request, id_ticket):
	ticket = Ticket.objects.get(pk=id_ticket) 
	
	#GET
	try:

		if request.method == 'GET':
			formulario_ingreso = TicketForm(instance=ticket)	
		else:
			formulario_ingreso = TicketForm(request.POST, instance=ticket)			
			encargado = EncargadoCliente.objects.get(codUsuario=request.user)
			ticket.codProyecto = Proyecto.objects.get(pk=request.POST.get('codProyecto'))
			ticket.codEncargadoCliente = encargado
			ticket.cliente = Cliente.objects.get(pk=encargado.cliente.pk)
			ticket.titulo = None if request.POST.get('titulo') == '' else request.POST.get('titulo')
			ticket.descripcion_ticket = None if request.POST.get('descripcion_ticket') == '' else request.POST.get('descripcion_ticket')
			ticket.comentario = None if request.POST.get('comentario') == '' else request.POST.get('comentario')
			ticket.prioridad = None if request.POST.get('prioridad') == '' else request.POST.get('prioridad')			
			ticket.UsuarioModificador = request.user
			if request.user.is_superuser:
				ticket.asignadoA = User.objects.get(pk=request.POST.get('asignadoA'))
				ticket.codEstado = Estado.objects.get(pk=request.POST.get('codEstado'))		

			ticket.save()

			remitente = 'ticket.soporte@bi-dss.com'
			destinatario = ticket.asignadoA.email;
			print destinatario
					
			msg = MIMEMultipart()

			msg['From'] = remitente
			msg['To'] = destinatario
			msg['Subject'] = '{0}{1}{2}'.format('TICKET #', ' ', ticket.pk)

			body = 'Saludos <b>{0}</b>,<br><br>una nueva solicitud le ha sido asignada.<br>Att.<b> Bi-DSS Technology.</b>'.format(ticket.asignadoA) 

			msg.attach(MIMEText(body.encode('utf-8'), 'html', 'utf-8'))
		
			username = 'ticket.soporte@bi-dss.com'
			password = 'Ticket2017'

			try:
				server = smtplib.SMTP('smtp.office365.com:587')
				server.starttls()
				server.login(username,password)
				server.sendmail(remitente, destinatario, msg.as_string())
				server.quit()
			except Exception as e:
				print e

			return redirect('listado_solicitudes')

	except Exception as e:
		print e

	ctx = {
		'formulario_ingreso': formulario_ingreso,		
	}	
	return render(request, 'ticket_editar.html', ctx)	


def ticket_detalle(request, id_ticket):
	detalle = Ticket.objects.get(id=id_ticket)

	return render(request, 'ticket_detalle.html', {'detalle': detalle})