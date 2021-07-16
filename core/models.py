from django.db import models
from django.utils.translation import gettext as _


class Chassi(models.Model):
    '''
    Cada chassi so pode se relacionar com um unico chassi
    '''
    numero = models.CharField(_('Chassi'), max_length=16, help_text=_('Maximo 16 caracteres'))

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Carro(models.Model):
    '''
    Cada carro só pode se relacionar com um chassi
    '''
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField(_('Modelo'), max_length=30, help_text=_('Maximo 30 caracteres'))
    preco = models.DecimalField(_('Preço'), max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "carro"
        verbose_name_plural = "carros"

    def __str__(self):
        return self.modelo

