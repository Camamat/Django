from django.shortcuts import render
from django.views.generic import TemplateView

def platform_func(request):
    return render(request, 'platform.html')

def menu(request):
    return render(request, 'menu.html')

def games_func(request):
    games = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay2"]}
    context = {
        'games' : games
    }
    return render(request, 'games.html', context)

def cart_func(request):
    return render(request, 'cart.html')