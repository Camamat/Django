from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def task_class(request):
    return render(request, 'class_template.html')

class task_func(TemplateView):
    template_name = 'func_template.html'