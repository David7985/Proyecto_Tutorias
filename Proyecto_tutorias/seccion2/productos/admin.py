from django.contrib import admin
from .models import Tutoria
# Register your models here.
# Título del panel
admin.site.site_header = "Administración de Tutorías"
admin.site.index_title = "Panel de Control"

# Configuración del modelo
class TutoriaAdmin(admin.ModelAdmin):
    list_display = ('asignatura', 'tema', 'fecha', 'modalidad', 'cupos')
    list_filter = ('modalidad',) # Filtro lateral
    search_fields = ('asignatura', 'tema') # Barra de búsqueda
# Esto permite que el admin gestione las tutorías desde admin
admin.site.register(Tutoria)