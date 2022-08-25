from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from .forms import Regg
# Create your views here.


def register(request):
    
    if request.method == 'POST':
        form=Regg(request.POST)
        if form.is_valid():
            user=form.save()
            
    form = Regg()
    context= {
        'forms':form,
    }
    return render(request, 'userapp/register.html',context)


# 