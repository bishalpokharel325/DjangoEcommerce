from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'frontend/pages/home.html', context)


def cart(request):
    context = {}
    return render(request, 'frontend/pages/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'frontend/pages/checkout.html', context)
