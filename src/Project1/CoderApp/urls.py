from django.urls import path
from CoderApp.views import read_home, read_courses, read_teacher, read_students, read_deliverables

urlpatterns = [
    path('home/', read_home),
    path('courses/', read_courses),
    path('teachers/', read_teacher),
    path('students/', read_students),
    path('deliverables/', read_deliverables),
]