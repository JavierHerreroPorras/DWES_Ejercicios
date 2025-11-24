from django.urls import path
from .views import new, search, search_all

urlpatterns = [
    path('new/', new),
    #path('all/', ),
    path('search/<int:id>/', search),
    path('search/', search_all)
]