from django.shortcuts import render

from django.views.generic import ListView, DetailView

# Create your views here.

from.models import  Libro

from django.http import HttpResponse



def busqueda_productos(request):

    return render(request, 'libro/busqueda_productos.html')

def buscar(request):
     
     mensaje="Articulo buscado: %r" %request.GET.get('prd')

     return HttpResponse(mensaje)



class listlibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabre_clave = self.request.GET.get("kword", '')
        #fecha 1
        f1 = self.request.GET.get("fecha1", '')
        #fecha 2
        f2 = self.request.GET.get("fecha2", '')

        if f1 and f2:
            return Libro.objects.listar_libros2(palabre_clave, f1, f2)
        else:
            return Libro.objects.listar_libros(palabre_clave)



class listlibrosTrg(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabre_clave = self.request.GET.get("kword", '')
        
        return Libro.objects.listar_libros_trg(palabre_clave)
        


class listlibros2(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista2.html'

    def get_queryset(self):
        
            return Libro.objects.listar_libros_categoria('1')
    

class LibroDetailView(DetailView):
     model = Libro
     template_name = "libro/detalle.html"


     
        

