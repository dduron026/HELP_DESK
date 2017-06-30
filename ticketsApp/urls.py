from django.conf.urls import url
from ticketsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	
	url(r'^ingreso_solicitud/', views.ingreso_solicitud, name='ingreso_solicitud'),
	url(r'^listado_solicitudes/', views.listado_solicitudes, name='listado_solicitudes'),
	url(r'^ticket/editar/(?P<id_ticket>\d+)/$', views.ticket_editar, name='ticket_editar'),
	url(r'^ticket/cerrar/(?P<id_ticket>\d+)/$', views.ticket_cerrar, name='ticket_cerrar'),


  
]