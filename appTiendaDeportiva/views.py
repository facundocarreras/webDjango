from django.shortcuts import render
from .models import TipoDeporte, TipoIndumentaria, Producto

def mostrarMaster(request):

    return render(request, 'masterPage.html')

def mostrarGestion(request):
    return render(request, 'forms/contacto.html')

def mostrarTipoDeporte(request):
    return render(request, 'forms/gestionDeporte.html')

def mostrarProducto(request):
    tiposDeporte = TipoDeporte.objects.all()
    tiposIndumentaria = TipoIndumentaria.objects.all()
    return render(request, 'forms/gestionProductos.html', {'tiposDeporte': tiposDeporte, 'tiposIndumentaria': tiposIndumentaria})

def monstrarTipoIndumentaria(request):
    return render(request, 'forms/tipoIndumentaria.html')

def buscarProducto(request):
    tiposDeporte = TipoDeporte.objects.all()
    tiposIndumentaria = TipoIndumentaria.objects.all()
    return render(request, 'forms/buscarProductos.html',  {'tiposDeporte': tiposDeporte, 'tiposIndumentaria': tiposIndumentaria})
        

def registrarTipoDeporte(request):
    nombre_deporte = request.POST['nombre_deporte']
    nuevoDeporte = TipoDeporte(detalle_deporte = nombre_deporte)
    nuevoDeporte.save()
    return render(request, 'forms/gestionDeporte.html')
    

def registrarIndumentaria(request):
    nombre_indumentaria = request.POST['nombre_indumentaria']
    nuevaIndumentaria = TipoIndumentaria(detalle_indumentaria = nombre_indumentaria)
    nuevaIndumentaria.save()
    return render(request, 'forms/tipoIndumentaria.html')



def registrarProducto(request):
    nombre_deporte = request.POST.get('select_deporte[]')
    nombre_indumentaria = request.POST.get('select_indumentaria[]')
    nombre_producto = request.POST['nombre_producto']
    stock = request.POST['stock']

    indumentariaN = TipoIndumentaria.objects.get(id = int(nombre_indumentaria))
    deporteN = TipoDeporte.objects.get(id = int(nombre_deporte))
    tipoProducto = Producto(nombre_producto = nombre_producto, tipo_deporte = deporteN, tipo_indumentaria = indumentariaN, stock = stock)
    tipoProducto.save()
    return render(request, 'forms/gestionProductos.html')

def confirmarBusqueda(request):
    tiposDeporte = request.GET.get('select_deporte[]')
    tiposIndumentaria = request.GET.get('select_indumentaria[]')

    productosFiltrados = Producto.objects.filter(tipo_deporte__pk = int(tiposDeporte)).filter(tipo_indumentaria__pk = int(tiposIndumentaria))
    return render(request, 'forms/resultadoBusqueda.html',  {'productos': productosFiltrados})