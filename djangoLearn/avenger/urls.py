from django.urls import path
from . import views

urlpatterns = [
    path('allhero/', views.allhero, name='allhero'),
]