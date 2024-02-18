from django.http import HttpResponse
from django.shortcuts import render
from CoderApp.models import Teachers, Students, Courses, Deliverables

def home(request):
    return render(request, 'CoderApp/home.html')

def courses(request):
    return render(request, 'CoderApp/courses.html')

def teachers(request):
    return render(request, 'CoderApp/teachers.html')

def read_teachers(request):
    print("View teacher") # Este recurso se usa para hacer debugs
    teacher = Teachers(nombre="John", apellido="Doe", email="doe@email.com")
    teacher.save()
    return HttpResponse("Los datos del profesor se guardaron exitosamente.")

def students(request):
    context = {
        'nombre': 'Yonathan',
        'apellido': 'Malczewski',
        'edad': 32,
        'cursos': ['Python',],
    }
    return render(request, 'CoderApp/students.html', context)

def deliverables(request):
    return render(request, 'CoderApp/deliverables.html')