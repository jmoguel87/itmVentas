from django.db import models
from django.conf import settings
from apps.core.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _

appLabel: str = 'articles'
    
class articles(AbstractBaseModel):
    codigoArt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    nombreArt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    descripcionArt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    unidadBaseArt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    unidadSatArt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    claveSatArt = models.CharField(max_length=settings.TEXTBOXMAXLENGTH, null=False)
    precioArt = models.DecimalField(max_digits=32, decimal_places=20, default=0.0, null=True)
    class Meta:                                                                                                                                                        
        app_label = appLabel
        ordering = ('codigoArt',)