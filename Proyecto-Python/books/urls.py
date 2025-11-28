from django.urls import path
from .views import new, search, search_all, sample_book_view

urlpatterns = [
    path('new/', new),
    #path('all/', ),
    path('search/<int:id>/', search),
    path('search/', search_all),
    path("sample-book/", sample_book_view, name="sample_book"),
]