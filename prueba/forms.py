from django import forms


class NombreMesForm(forms.Form):
    nombre_mes = forms.CharField(label='Nombre del mes', max_length=100)

class consulta1form(forms.Form):
    lat = forms.CharField(label = 'latitud', max_length = 100)
    lon = forms.CharField(label = 'longitud', max_length = 100)
    lat_hol = forms.CharField(label = 'holgura latitud', max_length = 100)
    lon_hol = forms.CharField(label= 'holgura longitud', max_length = 100)

class consulta2form(forms.Form):
    comentario= forms.CharField(label='comentario', max_length=100)

class consulta3form(forms.Form):
    mes = forms.CharField(label='Seleccione un mes del 1 (enero), al 12 (diciembre).', max_length=100)
