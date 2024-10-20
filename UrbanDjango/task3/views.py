from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def platform_func(request):
    return render(request, 'platform.html')

class games_func(TemplateView):
    template_name = 'games.html'

class cart_func(TemplateView):
    template_name = 'cart.html'