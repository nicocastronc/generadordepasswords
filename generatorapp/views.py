from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def password(request):
    #A traves de request podemos hacer una consulta por el metodo GET y acceder al atributo Length para saber su longitud.
    #Esto es un string, que es lo que muestra en la URL.
    longitud = int(request.GET.get('length'))
    caracteres = list('abcdefghijklmnopqrstuvwxyz')

    #Si mayusculas esta activado:
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    #Si numeros esta activado:
    if request.GET.get('numbers'):
        caracteres.extend(list('1234567890'))

    #Si caracteres espciales estan activados:
    if request.GET.get('special'):
        caracteres.extend(list('-*/,.+@!$%^&()#'))

    #Generamos la password con la 'Lista total' segun las opciones elegidas.
    pass_generada = ''
    for c in range(longitud):
        pass_generada += random.choice(caracteres)

    return render(request,'password.html',{'password':pass_generada})