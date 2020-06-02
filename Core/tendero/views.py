from .logic.logic_tendero import get_all_tenderos
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from monitoring.auth0backend import getRole
from pedidos.views import getPedidos
from reportes.views import get_productos_mayor_rotacion
from django.contrib.auth.decorators import login_required
from productoPedido.models import ProductoPedido
import requests

def get_tenderos(request):
    role = getRole(request)
    if request.user.is_authenticated and role == "CEO":
        tenderos = get_all_tenderos()
        tendero_list = serializers.serialize('json',tenderos)
        return HttpResponse(tendero_list, content_type='application/json')
    else:
        return HttpResponse("Unauthorized User")

def tenderoUI(request):
    return render(request, 'tenderoLogin.html')

@login_required
def tenderoListaPedidos(request):
    pedidos = getPedidos(request)
    pedidoProductos = []
    for pe in pedidos:
        productoPedidos = ProductoPedido.objects.filter(pedido = pe)
        for pp in productoPedidos:
            pedidoProductos.append(pp)

    context = {
            "pedidos": pedidos,
            "productosP": pedidoProductos
        }
    return render(request, 'listaPedidos.html', context)

@login_required
def tenderoListaCatalogo(request):
    productos = requests.get('http://ec2-54-164-131-230.compute-1.amazonaws.com:9898/catalogo')
    jsonprod = productos.json()
    
    context = {
            "productos": jsonprod
    }
    return render(request, 'listaCatalogo.html', context)

def tenderoListaRecomendados(request):
    productos = requests.get('http://52.23.227.195:8080/recomendados/recomendados')
    jsonprod = productos.json()
    context = {
        "productos": jsonprod
    }
    return render(request, 'listaRecomendados.html', context)

