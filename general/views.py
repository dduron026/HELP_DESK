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
from general.forms import *


def cerrar_sesion(request):
	logout(request)
	return redirect('login')

def login(request):

	ctx = {}
	logout(request)
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect(reverse('menu'))
		else:
			ctx = {
				 'error': True,
				 'username': username,
			}
	return render(request, 'login.html', ctx)

@login_required()
def menu(request):
	return render(request, 'base.html', {})	


def ingreso_solicitud(request):
	form = DetalleTicketForm()
	form2 = TicketForm()
	ctx = {
		'form':form,
		'form2': form2,
	}
	return render(request, 'nuevaSolicitud.html', ctx)	

def listado_solicitudes(request):
	return render(request, 'listadoSolicitudes.html', {})	


