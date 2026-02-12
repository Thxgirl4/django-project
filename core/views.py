from django.shortcuts import render
from .models import Product

def index(request):
    """print(dir(request.user))
    print(f'Headers: {request.headers}')
    print(f'User: {request.user}')"""
    produtos = Product.objects.all()
    print(produtos)

    context = {
        'curso': 'Django Framework',
        'produtos': produtos
    }
    return render (request, 'index.html', context)

def contact(request):
    return render (request, 'contatos.html')


def produto(request, pk):
    produto = Product.objects.get(pk=pk)
    context = {
        'produto': produto,
    }
    return render(request, 'produto.html', context)