from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError
from django.conf import settings

class frmCreateClient(forms.Form):
	codigoClt = forms.CharField(
		label=_('Código'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'text','placeholder':'Código','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
	razonSocialClt = forms.CharField(
		label=_('Razón Social'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Razón social', 'readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
	rfcClt = forms.CharField(
		label=_('R.F.C.'),
		# initial='',
		max_length = settings.RFCMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'R.F.C.','readonly':False,'maxlength':settings.RFCMAXLENGTH}),
		required=True,
	)
	regimenFiscalClt = forms.CharField(
		label=_('Regimen Fiscal'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Regimen Fiscal','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
	mainTelClt = forms.CharField(
		label=_('Telefono principal'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Telefono principal','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainEmailClt = forms.EmailField(
		label=_('Correo eléctronico principal'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.EmailInput(attrs={'class':'form-control','type':'email','placeholder':'hello@domain.com','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainCalleyCruzamientosClt = forms.CharField(
		label=_('Calle y cruzamientos'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Calle y cruzamientos','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainNumExtClt = forms.CharField(
		label=_('Num. Exterior'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Num. Exterior','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainNumIntClt = forms.CharField(
		label=_('Num. Interior'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Num. Interior','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainCpClt = forms.CharField(
		label=_('Código Postal'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Código Postal','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=True,
	)
	mainAsentamientoClt = forms.CharField(
		label=_('Asentamiento'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Asentamiento','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainLocalidadClt = forms.CharField(
		label=_('Localidad'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Localidad','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainMunicipioClt = forms.CharField(
		label=_('Municipio'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Municipio','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainEstadoClt = forms.CharField(
		label=_('Estado'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Estado','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)
	mainPaisClt = forms.CharField(
		label=_('País'),
		# initial='',
		max_length = settings.TEXTBOXMAXLENGTH,
		widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'País','readonly':False,'maxlength':settings.TEXTBOXMAXLENGTH}),
		required=False,
	)

	def __init__(self, *args, **kwargs):
		super(frmCreateClient, self).__init__(*args, **kwargs)

	def cleanCodigoClt(self):
		codigoClt = self.cleaned_data.get('codigoClt')
		if not codigoClt:
			raise ValidationError(_('You entered an invalid codigoClt.'))
		return codigoClt

	def cleanRazonSocialClt(self):
		razonSocialClt = self.cleaned_data.get('razonSocialClt')
		if not razonSocialClt:
			raise ValidationError(_('You entered an invalid razonSocialClt.'))
		return razonSocialClt
		
	def cleanRfcClt(self):
		rfcClt = self.cleaned_data.get('rfcClt')
		if not rfcClt:
			raise ValidationError(_('You entered an invalid rfcClt.'))
		return rfcClt
	
	def cleanRegimenFiscalClt(self):
		regimenFiscalClt = self.cleaned_data.get('regimenFiscalClt')
		if not regimenFiscalClt:
			raise ValidationError(_('You entered an invalid regimenFiscalClt.'))
		return regimenFiscalClt

	def cleanMainCpClt(self):
		mainCpClt = self.cleaned_data.get('mainCpClt')
		if not mainCpClt:
			raise ValidationError(_('You entered an invalid mainCpClt.'))
		return mainCpClt
	
	

	