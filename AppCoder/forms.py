

from django import forms

class SillonFormulario(forms.Form):    
    sillon = forms.CharField()
    precio = forms.IntegerField()
    

class MesaFormulario(forms.Form):    
    mesa = forms.CharField()
    precio = forms.IntegerField()
    color = forms.CharField()
    
class LamparaFormulario(forms.Form):    
    lampara = forms.CharField()
    precio = forms.IntegerField()
    tamaño = forms.CharField()