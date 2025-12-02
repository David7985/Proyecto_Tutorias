from django.shortcuts import get_object_or_404, redirect, render
from .models import Tutoria
from django.utils import timezone
from django.db import connection
from django.contrib.auth.decorators import login_required
from .forms import TutoriaForm

# Esta la dejamos pública para que cualquiera vea las clases
def lista_productos(request):
    tutorias = Tutoria.objects.all()
    context = {'tutorias': tutorias}
    return render(request, 'productos/obtener_productos.html', context)

def inicio(request):
    return render(request, 'productos/inicio.html')

def porId(request, id):
    tutoria = get_object_or_404(Tutoria, id=id)
    context = {'tutoria': tutoria}
    return render(request, 'productos/productos_mostrar.html', context)

# 2. AQUÍ PONEMOS LOS CANDADOS

@login_required
def eliminarId(request, id):
    tutoria = get_object_or_404(Tutoria, id=id)
    tutoria.delete()
    return redirect('lista_productos')

@login_required
def actualizarId(request, id):
    tutoria = get_object_or_404(Tutoria, id=id)
    if request.method == 'POST':
        form = TutoriaForm(request.POST, instance=tutoria)
        if form.is_valid():
            form.save()
            return redirect('producto_mostrar', id=tutoria.id)
    else:
        form = TutoriaForm(instance=tutoria)

    return render(request, 'productos/producto_actualizar.html', {'form': form, 'tutoria': tutoria})
@login_required
def agregarProducto(request):
    if request.method == 'POST':
        form = TutoriaForm(request.POST)
        if form.is_valid():
            tutoria = form.save(commit=False)
            tutoria.tutor = request.user # Asignamos el tutor automáticamente
            tutoria.save()
            return redirect('lista_productos')
    else:
        form = TutoriaForm()

    return render(request, 'productos/agregar_producto.html', {'form': form})



@login_required
def reporte_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.asignatura, p.tema, p.cupos, u.username, p.modalidad 
            FROM productos_tutoria p
            INNER JOIN auth_user u ON p.tutor_id = u.id     
            WHERE p.cupos > 0                            
            ORDER BY p.cupos DESC
        """)
        # Filtramos solo las tutorías que tienen cupos disponibles (WHERE)
        # Hacemos un JOIN entre la tabla de Tutorías y la de Usuarios
        resultados = cursor.fetchall()
    
    return render(request, 'productos/reporte_sql.html', {'resultados': resultados})