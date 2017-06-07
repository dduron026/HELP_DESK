from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout


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

def menu(request):
	return render(request, 'principal.html', {})	


def ingreso_solicitud(request):
	return render(request, 'nuevaSolicitud.html', {})	

def listado_solicitudes(request):
	return render(request, 'listadoSolicitudes.html', {})	