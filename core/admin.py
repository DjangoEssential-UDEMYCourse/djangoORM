from django.contrib import admin
from .models import Chassi, Carro


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):

    list_display = (
        'numero',
    )


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = (
        'modelo',
        'chassi',
        'preco',
    )
