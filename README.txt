# Consultas

carros = Carro.objects.all()
carro1 = carros.first()

Retorna tudo
motoristas = carro1.motoristas.all()

Retorna apenas o primeiro da lista
motos1 = carro1.motoristas.first()

Retorna um QuerySet
carros = Carro.objects.filter(motoristas=m1)

carros = Carro.objects.filter(motoristas__in = motos1).distinct()
