from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
        'message': 'Hola mundo desde la vista',
        'title': 'Productos',
        'products': [
            {'title':'Playera', 'price':5, 'stock':True},
            {'title': 'Camisa', 'price': 7, 'stock': True},
            {'title': 'mochila', 'price': 20, 'stock': False},
            {'title': 'laptop', 'price': 500, 'stock': False},
        ]
    })


def login(request):
    return render(request, 'users/login.html', {

    })