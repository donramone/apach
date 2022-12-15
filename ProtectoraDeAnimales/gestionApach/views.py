from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Inicio")

def castracion(request):
    return HttpResponse("Castracion")

def vacunacion(request):
    return HttpResponse("Vacunacion")

def veterinario(request):
    return HttpResponse("Veterinarios")

def contacto(request):
    return HttpResponse("Contaco")
