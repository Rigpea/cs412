# quotes/urls.py

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main, name='main'),  # Main page with random quote
    path('order/', views.order, name='order'),  # Show all quotes
    #path('about/', views.about, name='about'),  # About page
]