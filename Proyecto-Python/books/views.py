import json
from datetime import date
from pprint import pprint

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from books.models import Book, Author

import json

def home(request):
    return render(request, 'home.html')


def sample_book_view(request):
    # Tomamos el primer libro de la base de datos como ejemplo
    book = Book.objects.first()

    return render(request, "sample_book.html", {
        "book": book
    })

def get_json_request(request):
    """
    Devuelve el cuerpo JSON del request como dict.
    Si el body está vacío o es inválido, devuelve {}.
    """
    try:
        body = request.body.decode("utf-8")
        if not body:
            return {}
        return json.loads(body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}

@csrf_exempt
def new(request):
    body = get_json_request(request)

    a1 = Author.objects.get(pk=1)

    a1 = Book.objects.create(title=body.get("nombre"),
                        author=a1,
                        published_date=date(1967, 5, 30),
                        isbn="2"
                        )
    diccionario = model_to_dict(a1)
    return JsonResponse(diccionario)

def search(request, id):
    # Para pasar un objeto a JSON es necesario usar model_to_dict
    objecto_encontrado = Book.objects.get(id=id)
    diccionario = model_to_dict(objecto_encontrado)

    return JsonResponse(diccionario)

def search_all(request):
    # Query param: order=asc | desc
    order = request.GET.get("order", "asc")  # valor por defecto: ascendente

    if order == "desc":
        queryset = Book.objects.all().order_by("-published_date")
    else:
        queryset = Book.objects.all().order_by("published_date")

    return JsonResponse(list(queryset.values()), safe=False)
