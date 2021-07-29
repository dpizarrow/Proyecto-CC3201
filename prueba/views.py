from django.shortcuts import render
from django.http import HttpResponse
from prueba.models import Mes
from django.db import connection
from collections import namedtuple
from django.shortcuts import render
from .forms import NombreMesForm
from .forms import consulta1form
from .forms import consulta2form
from .forms import consulta3form
# Create your views here.

def index(request):
    return HttpResponse("Hola, soy una prueba.")


def mayo(request):
    return HttpResponse("El número del mes 'Mayo' es "+str(Mes.objects.filter(nombre='Mayo')[:1].get().numero))


def mayosql(request):
    return HttpResponse("El número del mes 'Mayo' es "+ str(consultar_mes('Mayo')[0].numero))

def mes(request):
    # si es POST, tenemos una petición del usuario
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NombreMesForm(request.POST)
        # verifica que sea valido:
        if form.is_valid():
            nombre_mes = form.cleaned_data['nombre_mes']
            sql_res = consultar_mes(nombre_mes)
            if sql_res:
                num_mes = consultar_mes(nombre_mes)[0].numero
                res = 'El número del mes '+nombre_mes+' es '+str(num_mes)
            else:
                res = 'El mes '+nombre_mes+' no está en la tabla'
            return render(request, 'mes_form.html', {'mes_form': form, 'resultados': res})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = NombreMesForm()
    return render(request, 'mes_form.html', {'mes_form': form})


def consultar_mes(mes):
    with connection.cursor() as cursor:
        cursor.execute("SELECT numero FROM test.mes WHERE nombre = %s", [mes])
        results = namedtuplefetchall(cursor)
    return results

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def consulta1(request):
    # si es POST, tenemos una petición del usuario
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = consulta1form(request.POST)
        # verifica que sea valido:
        if form.is_valid():
            lat = form.cleaned_data['lat']
            lon = form.cleaned_data['lon']
            lat_hol = form.cleaned_data['lat_hol']
            lon_hol = form.cleaned_data['lon_hol']            
            sql_res = consulta1_sql(lat,lon,lat_hol,lon_hol)
            if sql_res:
                res = consulta1_sql(lat,lon,lat_hol,lon_hol)
            else:
               res = 'Nada'
            return render(request, 'consulta1_form.html', {'consulta1_form': form, 'resultados': res})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = consulta1form()
    return render(request, 'consulta1_form.html', {'consulta1_form': form})

def consulta1_sql(lat,lon,lat_hol,lon_hol):
    with connection.cursor() as cursor:
        cursor.execute("SELECT lis.name,lis.room_type,lis.price, loc.lat,loc.lon FROM listings lis, location loc WHERE (%s <loc.lat) AND  (%s >loc.lat) AND (%s <loc.lon) AND  (%s >loc.lon) AND  loc.listing_id=lis.id ORDER BY price ASC FETCH FIRST 200 ROWS ONLY", [float(lat)-float(lat_hol)/2,float(lat)+float(lat_hol)/2,float(lon)-float(lon_hol)/2,float(lon)+float(lon_hol)/2])
        results = namedtuplefetchall(cursor)
    return results

def consulta2(request):
    # si es POST, tenemos una petición del usuario
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = consulta2form(request.POST)
        # verifica que sea valido:
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            sql_res = consulta2_sql(comentario)
            if sql_res:
                cons = consulta2_sql(comentario)
                res = cons
            else:
                res = 'Nada'
            return render(request, 'consulta2_form.html', {'consulta2_form': form, 'resultados': res})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = consulta2form()
    return render(request, 'consulta2_form.html', {'consulta2_form': form})


def consulta2_sql(comentario):
    with connection.cursor() as cursor:
        cursor.execute("SELECT list.name, list.price, rev.comments, loc.lat, loc.lon FROM listings list INNER JOIN reviews rev ON list.id = rev.listing_id INNER JOIN location loc ON list.id = loc.listing_id AND (rev.comments LIKE %s) ORDER BY price ASC FETCH FIRST 200 ROWS ONLY", ['%' + comentario + '%'])
        results = namedtuplefetchall(cursor)
    return results

def consulta3(request):
    # si es POST, tenemos una petición del usuario
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = consulta3form(request.POST)
        # verifica que sea valido:
        if form.is_valid():
            mes = form.cleaned_data['mes']
            sql_res = consulta3_sql(mes)
            if sql_res:
                cons = consulta3_sql(mes)
                res = cons
            else:
                res = 'Nada'
            return render(request, 'consulta3_form.html', {'consulta3_form': form, 'resultados': res})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = consulta3form()
    return render(request, 'consulta3_form.html', {'consulta3_form': form})


def consulta3_sql(mes):
    with connection.cursor() as cursor:
        cursor.execute("SELECT mv.promedio,mv.min_price, mv.max_price FROM precio_avg1 AS mv WHERE mv.month=%s",[mes])
        results = namedtuplefetchall(cursor)
    return results
