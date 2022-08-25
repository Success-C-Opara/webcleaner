from django.shortcuts import render
from . import views

# Create your views here.
def dash(request):
    return render(request, 'dashapp/index.html')


def fill(request): 
    
    return render(request, 'dashapp/form.html')