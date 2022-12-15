from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request ,"gestionApach/home.html")

def castracion(request):
    return render(request ,"gestionApach/castracion.html")

def vacunacion(request):
    return render(request ,"gestionApach/vacunacion.html")

def veterinario(request):
    return render(request ,"gestionApach/veterinario.html")

def contacto(request):
    return render(request ,"gestionApach/contacto.html")
