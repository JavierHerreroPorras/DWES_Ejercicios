from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book, Author


# Create your views here.
def new(request):
    a1 = Author.objects.get(pk=1)

    Book.objects.create(title="Cien años de soledad",
                        author=a1,
                        published_date=date(1967, 5, 30),
                        isbn="2"
                        )
    return HttpResponse("El libro se ha creado correctamente")