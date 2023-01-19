from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('sillones', views.sillones, name="Sillones"),
    path('mesas', views.mesas, name="Mesas"),
    path('lamparas', views.lamparas, name="Lamparas"),
    path('sillonFormulario', views.sillonFormulario, name="SillonFormulario"),
    path('mesaFormulario', views.mesaFormulario, name="MesaFormulario"),
    path('lamparaFormulario', views.lamparaFormulario, name="LamparaFormulario"),    
    path('busquedaModelos', views.busquedaModelos, name="BusquedaModelos"),
    path('buscarSillon/', views.buscarSillon),
    path('buscarMesa/', views.buscarMesa),
    path('buscarLampara/', views.buscarLampara)
]
