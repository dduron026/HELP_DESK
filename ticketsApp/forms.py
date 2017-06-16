
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.widgets import *
from django import forms
from general.models import *
from ticketsApp.models import *
from django.utils.translation import ugettext_lazy as _

PRIORIDAD = (
	('', '------'),
	('Baja', 'Baja'),
	('Media', 'Media'),
	('Alta', 'Alta'),
)



class TicketForm(ModelForm):
	titulo = forms.CharField(label='Título', required=True)
	prioridad = forms.ChoiceField(choices=PRIORIDAD, required=True)
	comentario = forms.CharField(widget=forms.Textarea(attrs={ 'rows':'4' ,'cols':'50'}), required=True)
	descripcion_ticket = forms.CharField(widget=forms.Textarea(attrs={ 'rows':'4' ,'cols':'50'}), label='Descripción', required=True)
	
	class Meta:
		model = Ticket
		fields = "__all__"
		exclude = []
		labels = {}

class ProyectoForm(ModelForm):

	nombre_proyecto  = forms.ModelChoiceField(queryset=Proyecto.objects.all(), label='Proyecto', required=True)
					

	class Meta:
		model = Proyecto
		fields = "__all__"
		exclude = []
		labels = {}		