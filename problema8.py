import random
#Notas:
#Valor Presente Neto (VPN) = -(Inversion Inicial (P)) + SumatoriaDe[Flujo Neto por Periodo (FNE) / Tasa de Descuento (i)
#En el problema no se menciona ninguna Tasa de Descuento (i) por lo que se considera que no existe

iteraciones = 5000          #Numero de inversiones simuladas
VPN = 0.0                   #TIR porque no existe la Tasa de Descuento
inversionInicial = 0.0

for i in range (iteraciones):
    #Calculando la inversion inicial a partir de su distribucion normal con d.estandar
    probabilidadInversionInicial = random.randint(1, 10000)
    if probabilidadInversionInicial <= 7:
        inversionInicial = 84000.0
    elif probabilidadInversionInicial <= 82:
        inversionInicial = 88000.0
    elif probabilidadInversionInicial <= 548:
        inversionInicial = 92000.0
    elif probabilidadInversionInicial <= 2119:
        inversionInicial = 96000.0
    elif probabilidadInversionInicial <= 5000:
        inversionInicial = 100000.0                 #Promedio
    elif probabilidadInversionInicial <= 7881:
        inversionInicial = 104000.0
    elif probabilidadInversionInicial <= 9452:
        inversionInicial = 108000.0
    elif probabilidadInversionInicial <= 9918:
        inversionInicial = 112000.0
    else:
        inversionInicial = 116000.0
        
    #Calculando el Valor Presente Neto (sumando el Flujo Neto de Efectivo ANUAL))
    sumatoriaFNE = 0.0
    for j in range(5):      #5 anios 
        probabilidadFNE = random.randint(1, 10000)
        if probabilidadFNE <= 4:
            sumatoriaFNE += 20000.0
        elif probabilidadFNE <= 39:
            sumatoriaFNE += 22000.0
        elif probabilidadFNE <= 228:
            sumatoriaFNE += 24000.0
        elif probabilidadFNE <= 918:
            sumatoriaFNE += 26000.0
        elif probabilidadFNE <= 2546:
            sumatoriaFNE += 28000.0
        elif probabilidadFNE <= 5000:
            sumatoriaFNE += 30000.0
        elif probabilidadFNE <= 7454:
            sumatoriaFNE += 32000.0
        elif probabilidadFNE <= 9082:
            sumatoriaFNE += 34000.0
        elif probabilidadFNE <= 9772:
            sumatoriaFNE += 36000.0
        elif probabilidadFNE <= 9961:
            sumatoriaFNE += 38000.0
        else:
            sumatoriaFNE += 40000.0
    
    #Una vez sumadas todas las FNE calculamos el VPN:
    VPN = -inversionInicial + sumatoriaFNE
#Al no tener una Tasa de Descuento se considera que la formula de VPN seria equivalente a la de TIR
#Si TIR > TRAM -> Aceptar proyecto
#TRAM = 30%

TRAM = inversionInicial * .3
if (VPN > TRAM):
    print("Se recomienda realizar la inversion.\nValor Neto Presente: {}".format(VPN))
else:
    print("No se recomienda realizar la inversion.\nValor Neto Presente: {}".format(VPN))
    
#Referencias sobre los conceptos de proyectos de inversion:
#http://moodle2.unid.edu.mx/dts_cursos_mdl/pos/AN/PI/S09/PI09_Visual.pdf
