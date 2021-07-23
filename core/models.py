from django.contrib.auth import get_user_model
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


class Montadora(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)

    class Meta:
        verbose_name = _('Montadora')
        verbose_name_plural = _('Montadoras')

    def __str__(self):
        return self.nome


def set_default_motadora():
    return Montadora.objects.get_or_create(nome="Padrão")[0] # retorna uma tupla (objeto, boolean)


class Carro(models.Model):
    '''
    # OneToOneField
    Cada carro só pode se relacionar com um chassi e um Chassi pode
    se relacionar apenas com um unico carro

    # ForeignKey (One To Many)
    Cada carro possui uma montadora, mas uma Montadora pode possuir varios
    carros

    # Many to Many
    Um carro pode ser dirigido por vários motoristas e
    Um motorista pode dirigir diversos carros porem não no
    mesmo tempo.
    '''
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_motadora))
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField(_('Modelo'), max_length=30, help_text=_('Maximo 30 caracteres'))
    preco = models.DecimalField(_('Preço'), max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "carro"
        verbose_name_plural = "carros"

    def __str__(self):
        return f'{self.montadora} {self.modelo}'
