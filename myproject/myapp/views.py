from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product 

# Create your views here.

def index(request):
    product= Product.objects.all()
    context ={
        'product':product
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        prize = request.POST.get('prize')
        sex = request.POST.get('prize')
        image = request.FILES['upload']
        products = Product(name=name,prize=prize,sex=sex,image=image)
        products.save() 

    return render(request, 'myapp/index.html',context)

def detail(request ,id):
    products = Product.objects.get(id=id)
    context = {
        'product':products
    }
    return render(request, 'myapp/detail.html', context)


def update(request,id):
    product= Product.objects.get(id=id)
    if request.method == 'POST':
        product.name=request.POST.get('name')
        product.prize=request.POST.get('prize')
        product.sex=request.POST.get('sex')
        product.image=request.FILES['upload']
    
        product.save()
        return redirect("/myapp/index")
    context={
        'products':product
    }
    return render(request, 'myapp/update.html', context)






