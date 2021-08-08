from django.urls import path

from . import views

urlpatterns = [
    path('myname/', views.name),
    path('', views.example, name='index'),
]
