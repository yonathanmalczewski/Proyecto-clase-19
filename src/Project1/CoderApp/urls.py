from django.urls import path
from CoderApp.views import home, courses, teachers, students, deliverables

urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('teachers/', teachers, name='teachers'),
    path('students/', students, name='students'),
    path('deliverables/', deliverables, name='deliverables'),
]