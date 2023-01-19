from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Sillon, Lamparas, Mesas
from AppCoder.forms import SillonFormulario, MesaFormulario, LamparaFormulario

# defino variables

def sillon(request):
      sillon =  Sillon(nombre="Polar", camada="50000")
      sillon.save()
      documentoDeTexto = f"--->Sillon: {sillon.nombre}   Precio: {sillon.precio}"
      return HttpResponse(documentoDeTexto)


def mesa(request):
      mesa =  Mesas(nombre="Nordica", precio="66000", color="Gris")
      mesa.save()
      documentoDeTexto = f"--->Mesa: {mesa.nombre}   Precio: {mesa.precio} Color: {mesa.color}"
      return HttpResponse(documentoDeTexto)


def lampara(request):
      lampara =  Lamparas(nombre="Punk", precio="20000", tamaño= "Medium")
      lampara.save()
      documentoDeTexto = f"--->Lampara: {lampara.nombre}   Precio: {lampara.precio} Tamaño: {lampara.tamaño}"
      return HttpResponse(documentoDeTexto)



# ubicacion HTML
def inicio(request):

      return render(request, "AppCoder/inicio.html")

def sillones(request):   
      
      return render(request, "AppCoder/sillones.html")

def mesas(request):

      return render(request, "AppCoder/mesas.html")


def lamparas(request):

      return render(request, "AppCoder/lamparas.html")


#FORMULARIOS COMPRA PRODUCTOS 

def sillonFormulario(request):
      if request.method == "POST":

            miFormulario = SillonFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  sillon = Sillon(nombre=informacion["sillon"], precio=informacion["precio"])
                  sillon.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = SillonFormulario()
 
      return render(request, "AppCoder/sillonFormulario.html", {"miFormulario": miFormulario})



def mesaFormulario(request):
      if request.method == "POST":

            miFormulario = MesaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  mesa = Mesas(nombre=informacion["mesa"], precio=informacion["precio"],color=informacion["color"] )
                  mesa.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = MesaFormulario()
 
      return render(request, "AppCoder/mesaFormulario.html", {"miFormulario": miFormulario})


def lamparaFormulario(request):
      if request.method == "POST":

            miFormulario = LamparaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  lampara = Lamparas(nombre=informacion["lampara"], precio=informacion["precio"],tamaño=informacion["tamaño"] )
                  lampara.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = LamparaFormulario()
 
      return render(request, "AppCoder/lamparaFormulario.html", {"miFormulario": miFormulario})

##

def busquedaModelos(request):
      return render(request, "AppCoder/busquedaModelos.html")



def buscarSillon(request):
      
      respuesta = f"Estoy buscando el precio del modelo de sillon: {request.GET['sillon']}"
      
      #No olvidar from django.http import HttpResponse
      
      return HttpResponse(respuesta)


def buscarMesa(request):
      
      respuesta = f"Estoy buscando el precio de la mesa: {request.GET['mesa']}"
      
      #No olvidar from django.http import HttpResponse
      
      return HttpResponse(respuesta)

def buscarLampara(request):
      
      respuesta = f"Estoy buscando el precio de la lampara: {request.GET['lampara']}"
      
      #No olvidar from django.http import HttpResponse
      
      return HttpResponse(respuesta)