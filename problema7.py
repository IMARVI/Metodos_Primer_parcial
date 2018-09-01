import random

iteraciones = 5000

#Inicializando una matriz que guardara las 35 combinaciones (politicas posibles):
matrizPoliticas = []
for i in range (7):
    matrizPoliticas.append([0] * 5)
    
for i in range (1, iteraciones + 1):
    for j in range(5, 12):
        nRevistas = j
        dinero = -1.5 * nRevistas
        
        #Primeros 10 dias
        probabilidadDemanda = random.randint(1, 100)
        if probabilidadDemanda <= 5:
            demanda = 5
        elif probabilidadDemanda <= 10:
            demanda = 6
        elif probabilidadDemanda <= 20:
            demanda = 7
        elif probabilidadDemanda <= 35:
            demanda = 8
        elif probabilidadDemanda <= 60:
            demanda = 9
        elif probabilidadDemanda <= 85:
            demanda = 10
        else:
            demanda = 11
        
        if demanda <= nRevistas:
            dinero += demanda * 2
            nRevistas -= demanda
        else:
            dinero += nRevistas * 2
            nRevistas = 0
            
        
        #Siguientes 20 dias
        for k in range(4, 9):
            nRevistas2 = nRevistas + k
            dinero += -1.2 * k
            
            probabilidadDemanda = random.randint(1, 100)
            if probabilidadDemanda <= 15:
                demanda = 4
            elif probabilidadDemanda <= 35:
                demanda = 5
            elif probabilidadDemanda <= 65:
                demanda = 6
            elif probabilidadDemanda <= 85:
                demanda = 7
            else:
                demanda = 8
            
            if demanda < nRevistas2:
                dinero = demanda * 2
                nRevistas2 -= demanda
                dinero = nRevistas2 * .6
            else:
                dinero = nRevistas2 * 2
            matrizPoliticas[j - 5][k - 4] += dinero

maxV = 0          
for i in range(0, 7):
    for j in range(0, 5):
        if (matrizPoliticas[i][j] > maxV):
            maxV = matrizPoliticas[i][j]
            x = i + 5
            y = j + 4
        print("Comprando {} revistas a $1.50 y {} a $1.20, la diferencia de dinero es de: {}".format(i + 5, j + 4,matrizPoliticas[i][j]))
print("\nLa mejor politica seria comprar {} libros el primer dia del mes y {} al pasar 10 dias".format(x, y))
