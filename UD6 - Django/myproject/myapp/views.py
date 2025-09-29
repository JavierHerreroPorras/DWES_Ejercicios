from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest, JsonResponse
from .models import Author, Book
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import ListView, DetailView
import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@require_GET
def restriccion_metodos(request):
    if request.method == "POST":
        # Se ha hecho una petición POST
        pass
    elif request.method == "GET":
        # Se ha hecho una petición GET
        pass

def devuelve_saludo(request):
    html = '<html><body>Hello, world!</body></html>'
    return HttpResponse(html)

def redirecciona_saludo(request):
    return redirect("saludo")

# Busca un libro por su ID. Si no existe, lanza Http404
def detalle_libro(request, id):
    libro = get_object_or_404(Book, id=id)
    return render(request, 'detalle_libro.html', {'libro': libro})

# Comprueba que el autor existe y busca todos sus libros.
# Si alguno de los dos no existe, lanza Http404
def libros_por_autor(request, autor_id):
    print(request.GET)
    print(request.META.get("HTTP_USER_AGENT"))
    autor = get_object_or_404(Author, id=autor_id)
    libros = get_list_or_404(Book, author=autor)
    return render(request, 'lista_libros_por_autor.html', {
        'autor': autor,
        'libros': libros
    })

# Equivalente a la vista de arriba
def libros_por_autor_excepciones(request, autor_id):
    try:
        autor = Author.objects.get(id=autor_id)
    except Author.DoesNotExist:
        raise Http404("Autor no encontrado")

    libros = Book.objects.filter(author=autor)
    if not libros.exists():
        raise Http404("Este autor no tiene libros registrados")

    return render(request, 'lista_libros_por_autor.html', {
        'autor': autor,
        'libros': libros
    })

# Busca un libro por su ID. Si no existe, lanza Http404.
# Devuelve los datos en JSON
def detalle_libro_json(request, id):
    libro = get_object_or_404(Book, id=id)
    datos = {
        'id': libro.id,
        'titulo': libro.title,
        'autor': libro.author.name
    }
    return JsonResponse(datos)

class AuthorListView(ListView):
    model = Author
    template_name = 'lista_autores.html'
    context_object_name = 'authors'                 # Nombre de la variable en el template


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'detalle_autor.html'
    context_object_name = 'author'                  # Nombre de la variable en el template

@method_decorator(csrf_exempt, name='dispatch')
class BookAPI(View):
    def get(self, request, book_id=None):
        if book_id:
            try:
                book = Book.objects.get(pk=book_id)
                data = {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author.name,
                    'published_date': str(book.published_date),
                    'isbn': book.isbn
                }
                return JsonResponse(data)
            except Book.DoesNotExist:
                return HttpResponseNotFound("Libro no encontrado")
        else:
            books = Book.objects.all().values(
                'id', 'title', 'author__name', 'published_date', 'isbn'
            )
            data = list(books)
            return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            datos = json.loads(request.body)
            autor = Author.objects.get(pk=datos['author_id'])  # Validación básica
            nuevo_libro = Book.objects.create(
                title=datos['title'],
                author=autor,
                published_date=datos['published_date'],
                isbn=datos['isbn']
            )
            return JsonResponse({'id': nuevo_libro.id}, status=201)
        except Author.DoesNotExist:
            return HttpResponseBadRequest("Autor no encontrado")
        except (KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest("Datos inválidos")
