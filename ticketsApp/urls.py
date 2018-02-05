from django.conf.urls import url
from ticketsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [	
	url(r'^ingresar_ticket/', views.ingresar_ticket, name='ingresar_ticket'),
	url(r'^listado_tickets/', views.listado_tickets, name='listado_tickets'),
	url(r'^ticket/editar/(?P<id_ticket>\d+)/$', views.ticket_editar, name='ticket_editar'),	
	url(r'^ticket_detalle/(?P<id_ticket>\d+)$', views.ticket_detalle, name='ticket_detalle'),
	  
]
