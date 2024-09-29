# restaurant/views.py

from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.




def main(request):
    context = {}
    return render(request, 'restaurant/templates/main.html', context)

def order(request):
    context = {}
    return render(request, 'restaurant/templates/order.html', context)
