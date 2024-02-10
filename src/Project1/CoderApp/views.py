from django.http import HttpResponse
from django.shortcuts import render
from CoderApp.models import Teachers

def read_home(request):
    return HttpResponse("View home")

def read_courses(request):
    return render(request, 'CoderApp/courses.html')

def read_teacher(request):
    print("View teacher") # Este recurso se usa para hacer debugs
    teacher = Teachers(nombre="John", apellido="Doe", email="doe@email.com")
    teacher.save()
    return HttpResponse("Los datos del profesor se guardaron exitosamente.") 

def read_students(request):
    context = {
        'nombre': 'Yonathan',
        'apellido': 'Malczewski',
        'edad': 32,
        'cursos': ['Python',],
    }
    return render(request, 'CoderApp/students.html', context)

def read_deliverables(request):
    return HttpResponse("View deliverables")

def index(request):
    return render(request, 'index.html')