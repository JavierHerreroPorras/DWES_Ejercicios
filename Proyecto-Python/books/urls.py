from django.contrib import admin
from django.urls import path, include
from books.views import *

urlpatterns = [
    path('new/', new),
    #path('all/', ),
    #path('filter/', )
]
