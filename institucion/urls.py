from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiantes', views.verEstudiantes, name='estudiantes'),
    path('docentes', views.verDocentes, name='docentes'),
]

handler404 = views.handler404
handler500 = views.handler500