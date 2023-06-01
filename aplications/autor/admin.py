from django.contrib import admin

# Register your models here.

from .models import Autor


class Autoradmin(admin.ModelAdmin):
    list_display = (
        'nombres',
        'nacionalidad',
        'id',
    )

    search_fields = ('nombres', 'nacionalidad', 'id',)
    list_filter = ('nombres', 'nacionalidad', 'id',)

    def __str__(self):
        return self.nombres


admin.site.register(Autor, Autoradmin)

