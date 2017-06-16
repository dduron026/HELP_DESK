
from django.contrib import admin

# Register your models here.

from .models import Ticket


class AdminTicket(admin.ModelAdmin):
	list_display = ["titulo", "comentario", "prioridad"]

	class Meta:
		model = Ticket

admin.site.register(Ticket, AdminTicket)
