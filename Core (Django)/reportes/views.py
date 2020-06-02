from django.shortcuts import render
from .logic.logic_reportes import get_productos_recomendados
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole, getUserEmail
from tendero.models import Tendero
###################################
from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId

@login_required
def get_productos_mayor_rotacion(request):
    role = getRole(request)
    email = getUserEmail(request)
    tendero = Tendero.objects.get(correo=email)
    if role == "Tendero Principal":
        productos = get_productos_recomendados(tendero.tienda.id)
        productos_list = serializers.serialize('json', productos)
        return productos


#Vista que permite encontrar los reportes dentro de una base de datos MongoDB

def getLatestReports():
    client = MongoClient(settings.MONGO_CLI)
    db = client.canemdb
    reportes = db['reportes']
    result = []
    data = reportes.find_one()
    jsonData = {
        'id': str(data['_id']),
        "zona_id": data['zona_id'],
        "fecha": data['fecha'],
        "descripcion": data['descripcion']
    }
    result.append(jsonData)
    client.close()
    return JsonResponse(result, safe=False)


@api_view(["GET", "POST"])
def reportes(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.canemdb
    reportes = db['reportes']
    if request.method == "GET":
        result = []
        data = reportes.find_one()
        #for dto in data:
        jsonData = {
            'id': str(data['_id']),
            "zona_id": data['zona_id'],
            "fecha": data['fecha'],
            "descripcion": data['descripcion'],
            "productoId": "1",
            "nombre": "Guaro",
            "precio": "5000",
            "descripcionProducto": "Pa emborrachar",
            "categoria": "Licores"
        }
        result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = reportes.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)
