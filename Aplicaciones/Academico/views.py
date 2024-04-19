from django.shortcuts import render,redirect
from .models import Curso

# Create your views here.

def home(request):

    materiaslistadas = Curso.objects.all()
    return render(request,"gestionCursos.html", {"materias" : materiaslistadas})

def registrarMateria(request):

    codigo=request.POST["txtCodigo"]
    nombre=request.POST["txtNombre"]
    horas_creditos=request.POST["numHorasCreditos"]

    materia=Curso.objects.create(codigo=codigo,nombre=nombre,horas_creditos=horas_creditos)
    return redirect('/')

def eliminarMateria(request,codigo):

    materia=Curso.objects.get(codigo=codigo)
    materia.delete()
    
    return redirect('/')

def edicionMateria(request,codigo):

    materia=Curso.objects.get(codigo=codigo)
    return render(request, "edicionMateria.html", {"materias": materia})

def editarMateria(request):

    codigo=request.POST["txtCodigo"]
    nombre=request.POST["txtNombre"]
    horas_creditos=request.POST["numHorasCreditos"]

    materia=Curso.objects.get(codigo=codigo)

    materia.nombre= nombre
    materia.horas_creditos=horas_creditos
    materia.save()

    return redirect('/')

def buscarMateria(request,codigo):

    materia=Curso.objects.get(codigo=codigo)
    return render(request, "buscarMateria.html", {"materias": materia})

def mostrarMateria(request):

    codigo=request.POST["txtCodigo"]
    materia=Curso.objects.get(codigo=codigo)

    materia.save()

    return redirect('/buscarMateria/'+codigo)