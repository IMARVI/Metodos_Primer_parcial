import random

dias = 260
costooDeInventario = 52
numInventario = 100
inventario = 100
costo = 0
costoBajo = 0
reodernar = 10
q = 0
for j in range(5):
    reodernar += 5
    for i in range(dias):

        if(inventario <= 10):
            inventario += reodernar
        r = random.random()
        if(r <= 0.02):
            demandaDiaria = 25
        elif(r > 0.02 and r <=0.06):
            demandaDiaria = 26
        elif(r > 0.06 and r <= 0.12):
            demandaDiaria = 27
        elif(r > 0.12 and r <= 0.24):
            demandaDiaria = 28
        elif(r > 0.24 and r <= 0.44):
            demandaDiaria = 29
        elif(r > 0.44 and r <= 0.68):
            demandaDiaria = 30
        elif(r > 0.68 and r <= 0.83):
            demandaDiaria = 31
        elif(r > 0.83 and r <= 0.93):
            demandaDiaria = 32
        elif(r > 0.93 and r <= 0.98):
            demandaDiaria = 33
        elif(r > 0.98 and r <= 1.00):
            demandaDiaria = 34
        r = random.random()
        if(r <= 0.20):
            tiempoEntrega = 1
        elif(r > 0.20 and r <=0.50):
            tiempoEntrega = 2
        elif(r > 0.50 and r <= 0.75):
            tiempoEntrega = 3
        elif(r > 0.75 and r <= 1.00):
            tiempoEntrega = 4
        r = random.random()
        if(r <= 0.40):
            tiempoEspera = 0
        elif(r > 0.40 and r <=0.60):
            tiempoEspera = 1
        elif(r > 0.60 and r <= 0.75):
            tiempoEspera = 2
        elif(r > 0.75 and r <= 0.90):
            tiempoEspera = 3
        elif(r > 0.90 and r <= 1.00):
            tiempoEspera = 4
        if(tiempoEspera < tiempoEntrega):
            demandaDiaria = 0
        costo += 100


        if(inventario > demandaDiaria):
            inventario-= demandaDiaria
        else:
            demandaDiaria -= inventario
            inventario = 0
            if(tiempoEspera < tiempoEntrega):
                costo += 50* demandaDiaria
            else:
                costo += 20* demandaDiaria

        if(inventario  == 0):
            costo+= costooDeInventario * numInventario

        if(i == 259):
            costo += 52 * inventario


    if(j == 0):
        costoBajo = costo
        q = reodernar
    else:
        if(costoBajo > costo):
            costoBajo = costo
            q = reodernar
    costo = 0

print("Cantidad óptima a ordenar (q): ", q)
