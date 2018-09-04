import numpy as np                              #Importando libreria para utilizar numero random poisson
import random

simulaciones = 5000                             #Numero de dias

costoPoliticaOrdenarCada8Dias = 0               #Costos
costoPoliticaOrdenar30Articulos = 0

inventarioPoliticaOrdenarCada8Dias = 30         #Inventarios
inventarioOrdenar30Articulos = 30

#Variables auxiliares
contador8Dias = 1                                   #Para ordenar cada 8 dias y reiniciar el contador
tiempoDeEntrega30Articulos = 0                      #Variable que guarda los dias que tardara el pedido en llegar
pedidoEnCaminoPoliticaOrdenar30Articulos = False    #Variable auxiliar porque en algunos casos la entrega se hace el mismo dia
tiempoDeEntrega8Dias = 0                            # ""
pedidoEnCaminoPolitica8Dias = False                 # ""
  
for i in range(simulaciones):
    #El siguiente if observa que no exista un pedido en camino, y si lo hay cuenta los dias para sumarlo al inventario (Politica de ordenar cuando mi inventario es < 10)
    if pedidoEnCaminoPoliticaOrdenar30Articulos:
        if tiempoDeEntrega30Articulos > 0:
            tiempoDeEntrega30Articulos -= 1
        else:
            pedidoEnCaminoPoliticaOrdenar30Articulos = False
            inventarioOrdenar30Articulos = 30
            tiempoDeEntrega30Articulos = 0
    
    #El siguiente if observa que no exista un pedido en camino, y si lo hay cuenta los dias para sumarlo al inventario (Politica de ordenar cada 8 dias)        
    if pedidoEnCaminoPolitica8Dias:
        if tiempoDeEntrega8Dias > 0:
            tiempoDeEntrega8Dias -= 1
        else:
            pedidoEnCaminoPolitica8Dias = False
            inventarioPoliticaOrdenarCada8Dias = 30
            tiempoDeEntrega8Dias = 0
    
    #Calculando la demanda con base en la distribucion binomial 
    probabilidadDemanda = random.randint(1, 10000)
    if probabilidadDemanda <= 930:
        demanda = 1
    elif probabilidadDemanda <= 3273:
        demanda = 2
    elif probabilidadDemanda <= 6398:
        demanda = 3
    elif probabilidadDemanda <= 8741:
        demanda = 4
    elif probabilidadDemanda <= 9671:
        demanda = 5
    else:
        demanda = 6
    
    #Restando la demanda a los inventarios:    
    inventarioOrdenar30Articulos -= demanda
    inventarioPoliticaOrdenarCada8Dias -= demanda
    
    #Sumando los costos de guardar los articulos en el almacen 
    costoPoliticaOrdenar30Articulos += inventarioOrdenar30Articulos
    costoPoliticaOrdenarCada8Dias += inventarioPoliticaOrdenarCada8Dias
    
    #Pasa un dia mas para la politica de ordenar cada 8 
    contador8Dias += 1
    
    #Politica de ordenar cuando el inventario sea < 10
    if inventarioOrdenar30Articulos <= 10:
        costoPoliticaOrdenar30Articulos += 50
        tiempoDeEntrega30Articulos = np.random.poisson(3)      #Numero poisson aleatorio con lambda = 3
        pedidoEnCaminoPoliticaOrdenar30Articulos = True
    
    #politica de ordenar cada 8 dias
    if contador8Dias == 8:
        contador8Dias = 1
        costoPoliticaOrdenarCada8Dias += 50
        tiempoDeEntrega8Dias = np.random.poisson(3)             #Numero poisson aleatorio con lambda = 3
        pedidoEnCaminoPolitica8Dias = True

#Imprimiendo resultado
if costoPoliticaOrdenar30Articulos < costoPoliticaOrdenarCada8Dias:
    print("La mejor politica es ordenar tu inventario cuando este sea menor a 10\nAhorro de: ${}".format(costoPoliticaOrdenarCada8Dias - costoPoliticaOrdenar30Articulos))
else:
    print("La mejor politica es ordenar tu inventario cada 8 dias\nAhorro de: ${}".format(costoPoliticaOrdenar30Articulos - costoPoliticaOrdenarCada8Dias))
