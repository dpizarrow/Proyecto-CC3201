from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mayosql/', views.mayosql, name='mayosql'),
    path('mayo/', views.mayo, name='mayo'),
    path('mes/', views.mes, name='mes'),
    path('consulta1/', views.consulta1, name='consulta1'),
    path('consulta2/', views.consulta2, name='consulta2'),
    path('consulta3/', views.consulta3, name='consulta2')
]

