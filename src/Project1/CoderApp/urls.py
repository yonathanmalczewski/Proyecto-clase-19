from django.urls import path
from CoderApp.views import read_teacher, read_students

urlpatterns = [
    path('teachers/', read_teacher),
    path('students/', read_students),
]