from django.db import models

from django.db.models import Q


class AutorManager(models.Manager):
    """Manager para el modelo Autor"""

    def listar_autores(self):
        """Lista todos los autores"""
        return self.all()

    def buscar_autor(self, kword):
        
        resultado = self.filter(nombre__icontains = kword)
        
        return resultado
    

    def buscar_autor2(self, kword):
        
        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)
        )
        
        return resultado
    
    def buscar_autor3(self, kword):
        
        resultado = self.filter(nombre_icontains=kword).filter(nombre__icontains = 35).exclude(edad=65)
        
        return resultado

    

    def buscar_autor4(self, kword):
        
        resultado = self.filter(
            edad_gt=40,
            edad_lt=65
        ).order_by('apellidos', 'nombre', 'id')
        
        return resultado
    
    
