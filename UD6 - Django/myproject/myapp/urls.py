from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
   # path('about/', views.about_view, name='about'),
   # path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
