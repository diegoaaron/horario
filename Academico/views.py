from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Curso

# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '!Cursos listados!')
    return render(request, 'gestionCursos.html', {"cursos":cursosListados})



def registrarcurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '!Curso registrado!')

    return redirect('/academico')



def eliminacionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)

    curso.delete()
    messages.success(request, '!Curso eliminado!')

    return redirect('/academico')



def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'edicionCurso.html', {"curso": curso})


def editarCurso(request):
    print(request)
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)

    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(request, '!Curso actualizado!')

    return redirect('inicio')

