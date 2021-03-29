from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
    
def index(request):
    return render(request,'infoInicio.html',{})

def verEstudiantes(request):
    estudiantes=[{'id_alumno':1, 'rut':'15665036', 'dv':'K','nombre':' Joaquin', 'apellido':' Lopez', 'carrera':'Analista Programador'},
          {'id_alumno':2, 'rut':'18987542', 'dv':'1','nombre':' Luis', 'apellido':' Rodriguez', 'carrera':'Analista Programador'},
          {'id_alumno':3, 'rut':'19745230', 'dv':'3','nombre':' Aldo', 'apellido':' Jerez', 'carrera':'Analista Programador'},
          {'id_alumno':4, 'rut':'16666874', 'dv':'9','nombre':' Lorenzo', 'apellido':' Suazo', 'carrera':'Ingeniería en Informática y Ciberseguridad'},
          {'id_alumno':5, 'rut':'18552369', 'dv':'8','nombre':' Pedro', 'apellido':' Lopez', 'carrera':'Construcción Civil'},
          {'id_alumno':6, 'rut':'14775115', 'dv':'1','nombre':' Ana', 'apellido':' Perez', 'carrera':'Prevención de Riesgos'},
          {'id_alumno':7, 'rut':'19855115', 'dv':'7','nombre':' Romina', 'apellido':' Zamorano', 'carrera':'Prevención de Riesgos'}]
    
    contexto = { 'estudiantes': estudiantes}
    
    return render(request,'verAlumnos.html',contexto)

def verDocentes(request):
    docentes=[{'id_profe':1, 'rut':'11052890', 'dv':'7','nombre':' Maria', 'apellido':' Moreno', 'curso':'Programación 1'},
          {'id_profe':2, 'rut':'13256666', 'dv':'K','nombre':' Ada', 'apellido':' Mallea', 'curso':'Algebra 1 y 2'},
          {'id_profe':3, 'rut':'14887789', 'dv':'0','nombre':' José', 'apellido':' Ramirez', 'curso':'Estructura de datos'},
          {'id_profe':4, 'rut':'9862335', 'dv':'6','nombre':' Julio', 'apellido':' Perez', 'curso':'Procesos Industriales'},
          {'id_profe':5, 'rut':'11478666', 'dv':'1','nombre':' Mario', 'apellido':' Soza', 'curso':'Administración y Finanzas'},
          {'id_profe':6, 'rut':'13788998', 'dv':'9','nombre':' Ana', 'apellido':' Andrade', 'curso':'Geotecnia'}]
    
    contexto = { 'docentes': docentes}
    
    return render(request,'verDocentes.html',contexto)

def handler404(request, exception):
    return render(request,'error.html',{})

def handler500(request):    
    return render(request,'500.html', {})
