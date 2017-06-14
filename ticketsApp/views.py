from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers  import make_password
from django.contrib.auth.models import User
from ticketsApp.forms import *


# Create your views here.


def ingreso_solicitud(request):
	
	formulario_ingreso = TicketForm()
	formulario_proyecto = ProyectoForm()

	ctx = {
	
		'formulario_ingreso': formulario_ingreso,
		'formulario_proyecto': formulario_proyecto,
	}
	return render(request, 'nuevaSolicitud.html', ctx)	


def listado_solicitudes(request):
	return render(request, 'listadoSolicitudes.html', {})





      # <form method="POST"> {% csrf_token %}
      #   {{form.as_p}}
      #   {{form2.as_p}}
          
      # </form> 


