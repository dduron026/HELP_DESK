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
 
 


def user_unicode_patch(self): #PARA MOSTRAR EL NOMBRE Y APELLIDO DEL USUARIO
	return '%s %s' % (self.first_name, self.last_name)

User.__unicode__= user_unicode_patch

@login_required()
def ingreso_solicitud(request):

	import smtplib
	
	formulario_ingreso = TicketForm()	
	if request.POST:
		ticket = Ticket()
		clientes = Cliente()
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

		fromaddr = 'denis.duron@bi-dss.com'
		toaddrs  = ['denisduron83@gmail.com', 'denis_duron@hotmail.com']
		# asunto = 'Nuevo Ticket Ingresado al sistema'
		msg = 'Correo enviado utilizando Python + Django BIDSS' 	 
		 
		# Datos
		username = 'denis.duron@bi-dss.com'
		password = 'Bidss2017'
		 
		# Enviando el correo

		server = smtplib.SMTP('smtp.office365.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr, toaddrs, msg)
		server.quit()


		ticket.save()

	ctx = {	
		'formulario_ingreso': formulario_ingreso,		
	}
	return render(request, 'nuevaSolicitud.html', ctx)	


@login_required()
def listado_solicitudes(request):

	lista = Ticket.objects.all().order_by('id')	
	return render(request, 'ticket_listado.html', {'lista':lista})



@login_required()
def ticket_cerrar(request):	
	return render(request, 'ticket_cerrar.html', {})

@login_required()
def ticket_editar(request, id_ticket):
	ticket = Ticket.objects.get(id=id_ticket)
	
	#GET
	if request.method == 'GET':
		formulario_ingreso = TicketForm(instance=ticket)	
	else:
		formulario_ingreso = TicketForm(request.POST, instance=ticket)			
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
		if request.user.is_superuser:
			ticket.asignadoA = User.objects.get(pk=request.POST.get('asignadoA'))

		ticket.save()
		return redirect('listado_solicitudes')
	ctx = {
		'formulario_ingreso': formulario_ingreso,		
	}	
	return render(request, 'ticket_editar.html', ctx)	


def ticket_detalle(request, id_ticket):
	detalle = Ticket.objects.get(id=id_ticket)

	return render(request, 'ticket_detalle.html', {'detalle': detalle})
		