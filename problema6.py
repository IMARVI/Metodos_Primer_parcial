import random
#Nota: formula utilizada -> z = (x - media)/d.estandar

horasPrueba = 20000
listaComponentesPoliticaCambioIndividual = [0, 0, 0, 0]
listaComponentesPoliticaCambioTotal = [0, 0, 0, 0]

costosConPoliticaIndividial = 0.0
costosConPoliticaTotal = 0.0

while horasPrueba > 0:
    for i in range(0, 3):                                           #Recorriendo los 4 componentes por politica
        listaComponentesPoliticaCambioIndividual[i] += 50           #Cada iteracion avanza 50 horas
        listaComponentesPoliticaCambioTotal[i] += 50
        falloComponente = False                                     #¿fallo el componente del indice actual?
        
        probabilidadFalloComponente = random.randint(1, 10000)
        #PoliticaIndividial:
        if listaComponentesPoliticaCambioIndividual[i] <= 300 and probabilidadFalloComponente < 13:
            falloComponente = True
        elif listaComponentesPoliticaCambioIndividual[i] == 400 and probabilidadFalloComponente < 215:
            falloComponente = True
        elif listaComponentesPoliticaCambioIndividual[i] == 500 and probabilidadFalloComponente < 1357:
            falloComponente = True
        elif listaComponentesPoliticaCambioIndividual[i] == 600 and probabilidadFalloComponente < 3415:
            falloComponente = True
        elif listaComponentesPoliticaCambioIndividual[i] == 700 and probabilidadFalloComponente < 3413:
            falloComponente = True
        elif listaComponentesPoliticaCambioIndividual[i] == 800 and probabilidadFalloComponente < 1359:
            falloComponente = True
        elif listaComponentesPoliticaCambioIndividual[i] >= 900 and probabilidadFalloComponente < 215:
            falloComponente = True 
        
        if falloComponente:
            listaComponentesPoliticaCambioIndividual[i] = 0
            costosConPoliticaIndividial += (200 + 100)       #Costo de unidad + costo de hora de servicio
        
        #PoliticaTotal:
        if listaComponentesPoliticaCambioTotal[i] <= 300 and probabilidadFalloComponente < 13:
            falloComponente = True
        elif listaComponentesPoliticaCambioTotal[i] == 400 and probabilidadFalloComponente < 215:
            falloComponente = True
        elif listaComponentesPoliticaCambioTotal[i] == 500 and probabilidadFalloComponente < 1357:
            falloComponente = True
        elif listaComponentesPoliticaCambioTotal[i] == 600 and probabilidadFalloComponente < 3415:
            falloComponente = True
        elif listaComponentesPoliticaCambioTotal[i] == 700 and probabilidadFalloComponente < 3413:
            falloComponente = True
        elif listaComponentesPoliticaCambioTotal[i] == 800 and probabilidadFalloComponente < 1359:
            falloComponente = True
        elif listaComponentesPoliticaCambioTotal[i] >= 900 and probabilidadFalloComponente < 215:
            falloComponente = True 
        
        if falloComponente:
            listaComponentesPoliticaCambioTotal = [0] * 4
            costosConPoliticaTotal += ((200 * 4) + (100 * 2))       #Costo de 4 unidades + costo de 2 horas de servicio  
        
        
    horasPrueba -= 50
    
if costosConPoliticaIndividial < costosConPoliticaTotal:
    print("La mejor politica es cambiar los componentes individualmente con un costo final de {} a las 20,000 horas. \nAhorrando: {}".format(costosConPoliticaIndividial, (costosConPoliticaTotal - costosConPoliticaIndividial)))
else:
    print("La mejor politica es cambiar todos los componentes al primer incidente con un costo final de {} a las 20,000 horas. \nAhorrando: {}".format(costosConPoliticaTotal, (costosConPoliticaIndividial - costosConPoliticaTotal)))
