from django.urls import path
from appTiendaDeportiva import views

urlpatterns = [
    # Muestra forms
    path('master/', views.mostrarMaster),
    path('gestion/', views.mostrarGestion),
    path('tipoDeporte/', views.mostrarTipoDeporte),
    path('tipoIndumentaria/', views.monstrarTipoIndumentaria),
    path('gestionProducto/', views.mostrarProducto),
    path('buscarProducto/', views.buscarProducto),
    path('confirmarBusqueda/', views.confirmarBusqueda),

    # Puntos de registro
    path('registrarDeporte/', views.registrarTipoDeporte, name = 'registrarDeporte'),
    path('registrarIndumentaria/', views.registrarIndumentaria, name = 'registrarIndumentaria'),
    path('registrarProductos/', views.registrarProducto),
    
]
