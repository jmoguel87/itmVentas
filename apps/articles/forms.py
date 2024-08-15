from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError
from django.conf import settings

class frmCreateArticle(forms.Form):
    codigoArt = forms.CharField(
		label=_('Código'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'text','placeholder':'Código','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
    nombreArt = forms.CharField(
		label=_('Nombre'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'text','placeholder':'Nombre','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
    descripcionArt = forms.CharField(
		label=_('Descripción'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'text','placeholder':'Descripción','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
    unidadBaseArt = forms.CharField(
		label=_('Unidad base'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'text','placeholder':'Unidad base de medida interna','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
    unidadSatArt = forms.CharField(
		label=_('Undad SAT'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'text','placeholder':'Clave unidad de medida SAT','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
    claveSatArt = forms.CharField(
		label=_('Clave articulo SAT'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'text','placeholder':'Código del articulo del SAT','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
    precioArt = forms.FloatField(
		label=_('Precio'),
		widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','type':'numeric','placeholder':'Precio','readonly':False,'step_size': "0.00"}),
		required=True,
	)
    
    def __init__(self, *args, **kwargs):
        super(frmCreateArticle, self).__init__(*args, **kwargs)

    def cleanCodigoArt(self):
        codigoArt = self.cleaned_data.get('codigoArt')
        if not codigoArt:
            raise ValidationError(_('You entered an invalid codigoArt.'))
        return codigoArt