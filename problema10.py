from random import random
from math import ceil

inventario = 0
tiempoDeOrden = 0
orden = 0
espera = 0
faltantes = 0
faltantesTot = 0
ordenEnEspera = False
inventario = 15
limite = 5

for dia in range(0,260):

    if tiempoDeOrden == 0 and ordenEnEspera == True:
        inventario += 15
        orden += 1
        ordenEnEspera = False


    if inventario <= limite and not ordenEnEspera:

        tiempoDeOrden = random()
        if tiempoDeOrden <= 0.25:
            tiempoDeOrden = 1
        elif tiempoDeOrden > 0.25 and tiempoDeOrden <= 0.75:
            tiempoDeOrden = 2
        elif tiempoDeOrden > 0.75 and tiempoDeOrden <= 0.95:
            tiempoDeOrden = 3
        else:
            tiempoDeOrden = 4
        ordenEnEspera = True





    dailyDemand = random()
    if dailyDemand <= 0.04:
        dailyDemand = 0
    elif dailyDemand > 0.04 and dailyDemand <= 0.1:
        dailyDemand = 1
    elif dailyDemand > 0.1 and dailyDemand <= 0.2:
        dailyDemand = 2
    elif dailyDemand > 0.2 and dailyDemand <= 0.4:
        dailyDemand = 3
    elif dailyDemand > 0.4 and dailyDemand <= 0.7:
        dailyDemand = 4
    elif dailyDemand > 0.7 and dailyDemand <= 0.88:
        dailyDemand = 5
    elif dailyDemand > 0.88 and dailyDemand <= 0.96:
        dailyDemand = 6
    elif dailyDemand > 0.96 and dailyDemand <= 0.99:
        dailyDemand = 7
    else:
        dailyDemand = 8


    if tiempoDeOrden > 0:
        tiempoDeOrden -= 1
        if inventario < dailyDemand:
            dailyDemand = dailyDemand - inventario
            inventario = 0

            faltantes += dailyDemand
            faltantesTot += dailyDemand

        elif inventario > dailyDemand:
            inventario -= dailyDemand
            espera += inventario
    else:
        if inventario > dailyDemand:
            inventario -= dailyDemand
            espera += inventario


print("Se ordenan de nuevo el stock:",limite )
print("Costo de ordenar: $", orden*50)
print("Costo de espera: $",espera*26)
print("Costo de faltante $",faltantesTot*25)