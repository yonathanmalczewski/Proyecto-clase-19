from django.http import HttpResponse
from django.shortcuts import render
from CoderApp.models import Teachers

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
    return render(request, 'template1.html', context)