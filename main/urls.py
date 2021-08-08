from django.urls import path

from . import views

urlpatterns = [
    path('myname/', views.name),
    path('example-html/', views.example_html),
    path('', views.example, name='index'),
]
