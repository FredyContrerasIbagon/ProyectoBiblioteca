from django.contrib import admin

# Register your models here.

from .models import Libro, Categoria


class LibroAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'fecha',
        'categoria',        
    )
    search_fields = ('titulo', 'fecha', 'categoria',)
    list_filter = ('fecha', 'categoria',)

    def get_ordering(self, request):
        return ['titulo']

    


admin.site.register(Libro, LibroAdmin)
admin.site.register(Categoria)