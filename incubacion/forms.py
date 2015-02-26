from django import forms
from incubacion.models import Incubacion


class IncubacionForm(forms.ModelForm):
    class Meta:
        model=Incubacion
        fields = ["alcance","condiciones","descripcion","nombre","perfilOfertas"]

