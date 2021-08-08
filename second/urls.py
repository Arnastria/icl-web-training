from django.urls import path

from . import views

urlpatterns = [
    path('time/', views.display_time),
    path('', views.index)
]
