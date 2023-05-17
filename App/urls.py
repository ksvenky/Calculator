from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('authors', views.authors, name='authors'),
    path('scientific-calculator', views.scientific_calculator, name='scientific_calculator'),
]
