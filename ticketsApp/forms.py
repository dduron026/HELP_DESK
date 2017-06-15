
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.widgets import *
from django import forms
from general.models import *
from ticketsApp.models import *
from django.utils.translation import ugettext_lazy as _

PRIORIDAD = (
	('', '------'),
	('Poca', 'Baja'),
	('Mucha', 'Media'),
	('Extrema', 'Alta'),
)



class TicketForm(ModelForm):
	
	prioridad = forms.ChoiceField(choices=PRIORIDAD, required=False)
	comentario = forms.CharField(widget=forms.Textarea(attrs={ 'rows':'4' ,'cols':'50'}), required=False)
	descripcion_ticket = forms.CharField(widget=forms.Textarea(attrs={ 'rows':'4' ,'cols':'50'}), label='Descripción', required=False)
	class Meta:
		model = Ticket
		fields = "__all__"
		exclude = []
		labels = {
			
			'titulo': _('Titulo del Ticket'),
					
		}

class ProyectoForm(ModelForm):

	nombre_proyecto  = forms.ModelChoiceField(queryset=Proyecto.objects.all(), label='Proyecto', required=False)
					

	class Meta:
		model = Proyecto
		fields = "__all__"
		exclude = []
		labels = {}		