from django.http import HttpResponse
from django.template import Template, context
from django.template import loader
from django.shortcuts import render
from floresApp.models import producto
def home(request):
    paginaDeInicio = loader.get_template('inicio.html')
    renderInicio = paginaDeInicio.render()
    return HttpResponse(renderInicio)
def info(request):
    paginaInfo = loader.get_template('informacion.html')
    renderInformacion = paginaInfo()
    return HttpResponse(renderInformacion)
def conctato(request):
    return render(request, 'conctacto.html')
def busqueda(request):
    return render(request, "busqueda.html")
def resultadobusqueda(request):
    if request.GET["nombreProducto"]:
        articulo = request.GET["nombreProducto"]
        Aproducto = producto.objects.filter(nombre__icontains=articulo) 
        return render(request, 
                      "resultadobusqueda.html",
                      {"articulo":Aproducto,
                      "query":articulo})   
    else:
        mensaje = "El producto no se encuentra"
    return HttpResponse(mensaje)