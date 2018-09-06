import random

clientes = 10 
perdidos = 0
estacionados = 0
estacionado = 0
disponibles = 0
h = 24
m = 60 
    
for hora in range(h):
    s = []
    carros = []
    lugares = 6
    for i in range (clientes):
        m1 = random.randint(1,60)
        carros.append(m1)
    carros.sort()
    for i in range (clientes):
        tiempo = random.randint(10,30)
        s.append(tiempo + carros[i])

    for i in range (m):
        for coche in range (clientes):
            if(carros[coche] == i):
                if(lugares > 0):

                    estacionados += 1
                    lugares -= 1
                else:

                    perdidos += 1
            if(s[coche] == i):

                lugares +=  1

    disponibles += lugares

promedio_estacionado = float(estacionados)/(clientes*h)
promedio_perdido = float(perdidos)/(clientes*h)
promedio_disponible = float(disponibles)/(6*h)

porcentaje_perdidos = (estacionados*100)/clientes
porcentaje_promedio_disponibles = round(promedio_disponible*100, 2)
probabilidad_lugar = round(promedio_estacionado,3)


print("% perdidos: ", porcentaje_perdidos)
print("% promedio disponibles: ", porcentaje_promedio_disponibles)
print(" probabilidad de encontrar lugar", probabilidad_lugar)
