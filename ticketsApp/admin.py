
from django.contrib import admin

# Register your models here.

from .models import *




class AdminTicket(admin.ModelAdmin):
	list_display = ["titulo", "comentario", "prioridad"]

	class Meta:
		model = Ticket

admin.site.register(Ticket, AdminTicket)

admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(EncargadoCliente)