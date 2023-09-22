from django.urls import path
from . import views 
urlpatterns = [
    path('', views.clientes, name='clientes')  
]

# models views e templates