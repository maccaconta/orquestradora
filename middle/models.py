from common.base_model import BaseModel
from django.db import models


class CityCode(BaseModel):
    """
             Name            : CityCode
            :class           : Classe Recipient
            :create          : setembro-2021
            :Models          : auto complete, text and email
            description      : faz...
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    city_code = models.CharField('código', max_length=16, default='')
    city_name = models.CharField('cidade', max_length=128, default='')
    
    class Meta:
        verbose_name_plural = 'Códigos Cidades'
        verbose_name = 'Código Cidade'


class CountryCode(BaseModel):
    """
             Name            : CityCode
            :class           : Classe Recipient
            :create          : setembro-2021
            :Models          : auto complete, text and email
            description      : faz...
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    country_code = models.CharField('código', max_length=64, default='')
    country_name = models.CharField('país', max_length=128, default='')
    
    class Meta:
        verbose_name_plural = 'Códigos Paises'
        verbose_name = 'Código País'
