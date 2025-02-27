from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages

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


def login_view(request):
    username = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            msg = 'Bienvenido'.format((user.username))
            messages.success(request, msg)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o Contraseña, no válidos')

    return render(request, 'users/login.html', {
        'message': messages,
    })