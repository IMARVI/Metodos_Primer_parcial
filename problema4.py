import random
#Notas:
#    Z = (x - x(media))/d.estandar
#    d.estandar = sqrt(varianza)

simulaciones = 100000
interferencias = 0.0

for i in range(simulaciones):
    #Vamo' a ver cuanto mide el cojinete:
    probabilidadCojinete = random.randint(1, 10000)
    if probabilidadCojinete <= 13:
        medidaCojinete = 1.38
    elif probabilidadCojinete <= 62:
        medidaCojinete = 1.40
    elif probabilidadCojinete <= 228:
        medidaCojinete = 1.42
    elif probabilidadCojinete <= 668:
        medidaCojinete = 1.44
    elif probabilidadCojinete <= 1587:
        medidaCojinete = 1.46
    elif probabilidadCojinete <= 3085:
        medidaCojinete = 1.48
    elif probabilidadCojinete <= 5000:          #Promedio
        medidaCojinete = 1.50
    elif probabilidadCojinete <= 6915:
        medidaCojinete = 1.52
    elif probabilidadCojinete <= 8413:
        medidaCojinete = 1.54
    elif probabilidadCojinete <= 9332:
        medidaCojinete = 1.56
    elif probabilidadCojinete <= 9772:
        medidaCojinete = 1.58
    elif probabilidadCojinete <= 9938:
        medidaCojinete = 1.60
    else:
        medidaCojinete = 1.62
    #Ahora vamo' a ver cuanto mide la flecha:
    probabilidadFlecha = random.randint(1, 10000)
    if probabilidadFlecha <= 6:
        medidaFlecha = 1.38
    elif probabilidadFlecha <= 38:
        medidaFlecha = 1.40
    elif probabilidadFlecha <= 228:
        medidaFlecha = 1.42    
    elif probabilidadFlecha <= 918:
        medidaFlecha = 1.44
    elif probabilidadFlecha <= 2514:
        medidaFlecha = 1.46
    elif probabilidadFlecha <= 5000:        #Promedio
        medidaFlecha = 1.48
    elif probabilidadFlecha <= 7486:
        medidaFlecha = 1.50
    elif probabilidadFlecha <= 9082:
        medidaFlecha = 1.52
    elif probabilidadFlecha <= 9772:
        medidaFlecha = 1.54
    elif probabilidadFlecha <= 9962:
        medidaFlecha = 1.56
    else:
        medidaFlecha = 1.58
    
    if medidaFlecha >= medidaCojinete:
        interferencias += 1
        
print("EL numero de interferencias dentro de {} simulaciones es: {}".format(simulaciones, interferencias))
print("Probabilidad de interferencia: {}".format(interferencias/simulaciones))