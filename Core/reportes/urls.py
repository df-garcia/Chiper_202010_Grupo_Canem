from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    path('list/', views.get_productos_mayor_rotacion, name='productoList'),
    url(r'^recomendados/$', reportes),
    #path('recomendados/', views.getLatestReports, name = "reportesURL")
]