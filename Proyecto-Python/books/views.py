import json
from datetime import date
from pprint import pprint

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from books.models import Book, Author

import json

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

# Create your views here.
def new(request):
    a1 = Author.objects.get(pk=1)

    Book.objects.create(title="Cien años de soledad",
                        author=a1,
                        published_date=date(1967, 5, 30),
                        isbn="2"
                        )
    return HttpResponse("El libro se ha creado correctamente")

# @csrf_exempt --> Importante
def search(request, id):
    #pprint(request.__dict__)
    #body = get_json_request(request)
    #print(body)
    #print(request.method)

    # Para pasar un objeto a JSON es necesario usar model_to_dict
    objecto_encontrado = Book.objects.get(id=id)
    diccionario = model_to_dict(objecto_encontrado)

    return JsonResponse(diccionario)

def search_all(request):
    # Para pasar un listado de objetos a JSON es necesario usar:
        # .values() --> Acepta parámetros --> .values("id", "title")
        # safe=False en JsonResponse, para que acepte una lista.
        # Es necesario convertir el Queryset en lista con list()
    return JsonResponse(list(Book.objects.all().values()), safe=False)