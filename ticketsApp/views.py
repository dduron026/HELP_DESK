from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout

from django.contrib.auth.models import User
from ticketsApp.forms import *
from .models import * 


# Create your views here.


def ingreso_solicitud(request):
	
	formulario_ingreso = TicketForm()
	formulario_proyecto = ProyectoForm()
	# GET

	#POST
	if request.POST:
		ticket = Ticket()
		clientes = Cliente()
		proyecto = Proyecto()
		encargado = EncargadoCliente.objects.get(codUsuario=request.user)
		ticket.codProyecto = Proyecto.objects.get(pk=request.POST.get('nombre_proyecto'))
		ticket.codEncargadoCliente = encargado
		ticket.cliente = Cliente.objects.get(pk=encargado.cliente.pk)
		ticket.codEstado = Estado.objects.get(pk=1)



		print ticket.codProyecto
		ticket.titulo = None if request.POST.get('titulo') == '' else request.POST.get('titulo')
		ticket.descripcion_ticket = None if request.POST.get('descripcion_ticket') == '' else request.POST.get('descripcion_ticket')
		ticket.comentario = None if request.POST.get('comentario') == '' else request.POST.get('comentario')
		ticket.prioridad = None if request.POST.get('prioridad') == '' else request.POST.get('prioridad')
		
		ticket.save()

	ctx = {
	
		'formulario_ingreso': formulario_ingreso,
		'formulario_proyecto': formulario_proyecto,
		
	}
	return render(request, 'nuevaSolicitud.html', ctx)	


def listado_solicitudes(request):
	return render(request, 'listadoSolicitudes.html', {})







