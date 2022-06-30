from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contacto

from .forms import contactoForm 

# Create your views here.

def inicio(request):   
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def agenda(request):
    contactos = contacto.objects.all()
    return render(request,'agenda/index.html',{'contactos': contactos})

def crear(request):
    formulario = contactoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('agenda')
    return render(request,'agenda/crear.html',{'formulario': formulario})

def editar(request, id):
    contactoe = contacto.objects.get(id=id)
    formulario = contactoForm(request.POST or None, request.FILES or None, instance=contactoe)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('agenda')
    return render(request,'agenda/editar.html',{'formulario':formulario}) 

def eliminar(request, id):
    contactod = contacto.objects.get(id=id)
    contactod.delete()
    return redirect ('agenda')    