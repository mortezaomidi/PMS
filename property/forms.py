from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget


from .models import Property

class PropertyForm(forms.Form):
    class Meta:
        model = Property
        exclude = ['user']
        widgets = {'geom': LeafletWidget()}
