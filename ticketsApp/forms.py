from django.forms import ModelForm
from django.forms.widgets import *
from django import forms
from general.models import *
from ticketsApp.models import *
from django.utils.translation import ugettext_lazy as _

URGENCIA = (
	('', '------'),
	('Poca', 'Baja'),
	('Mucha', 'Media'),
	('Extrema', 'Alta'),
)



class TicketForm(ModelForm):

	comentario = forms.CharField(widget=forms.Textarea(attrs={ 'rows':'4' ,'cols':'50'}), required=False)

	class Meta:
		model = Ticket
		fields = "__all__"
		exclude = []
		labels = {
			
			'titulo': _('Titulo del Ticket'),
			

		
		}

class DetalleTicketForm(ModelForm):

	descripcion_ticket = forms.CharField(widget=forms.Textarea(attrs={ 'rows':'4' ,'cols':'50'}), required=False)
	prioridad = forms.ChoiceField(choices=URGENCIA, label='Prioridad del Ticket')

	class Meta:
		
		model = DetalleTicket
		fields = "__all__"
		exclude = ['codTicket', 'estadoDetalleTickets', 'asignadoA'  ]
		labels = {
			'prioridad': _('Prioridad'),
			'archivo': _('Adjuntar Archivo'),
			'descripcion_ticket': _('Incidente'),
		
		}