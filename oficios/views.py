from django.shortcuts import render, redirect

from .forms import MascotaForm

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'oficios/index.html')

# primer formulario 
def mascota_view(request):
    if request.method == 'POST':
        
        form = MascotaForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('oficios:index')

    else:
        form = MascotaForm()

    return render(request, 'oficios/generaoficio.html', {'form':form})

def busqueda_productos(request):
    return render(request, 'oficios/busqueda_productos.html')


def buscar(request):
    mensaje = "artículo buscado: %r" %request.GET["prd"]

    return HttpResponse(mensaje)