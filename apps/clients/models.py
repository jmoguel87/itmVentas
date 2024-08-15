from django.db import models
from django.conf import settings
from apps.core.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _

appLabel: str = 'clients'

class clients(AbstractBaseModel):
    codigoClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    razonSocialClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    rfcClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    regimenFiscalClt = models.CharField(max_length=settings.RFCMAXLENGTH, null=False)
    mainTelClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    mainEmailClt = models.EmailField(blank=True, max_length=settings.TEXTBOXMAXLENGTH, null=True, default='')
    mainCalleyCruzamientosClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    mainNumExtClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    mainNumIntClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    mainCpClt = models.CharField(max_length=settings.RFCMAXLENGTH, null=False)
    mainAsentamientoClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    mainLocalidadClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    mainMunicipioClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    mainEstadoClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    mainPaisClt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=True)
    class Meta:                                                                                                                                                        
        app_label = appLabel
        ordering = ('codigoClt',)