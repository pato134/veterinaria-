from django.conf.urls import url, include
from . import views

urlpatterns = [
	#url(r'^$', views.mostrar_inicio),
	
    url(r'^nuevo/$', views.producto_nuevo, name='productos_crear'),
    url(r'^listar_agricolas/$', views.listar_agricolas, name='listar_agricolas'),
    url(r'^listar_productos/$', views.listar_productos, name='listar_productos'),
    url(r'^listar_accesorios/$', views.listar_accesorios, name='listar_accesorios'),
    url(r'^gestionar_proformas/$', views.gestionar_proformas, name='gestionar_proformas'),
    url(r'^gestionar_factura/$', views.gestionar_factura, name='gestionar_factura'),
]