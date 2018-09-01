import random


iteraciones = 5
s = 86400
c = 40
o1 = ocupado2 = ocupado3 = 0
tf1 = tiempofila2 = tiempofila3 = 0
formados = catendidos = clienteensistema = 0
tSistema = 0

for hora in range(iteraciones):
    for i in range(s):
        if (i % 90 == 0):
            formados += 1

        if (formados > 0 and o1 == 0):
            catendidos += 1
            formados -= 1
            o1 = 1
            t = random.randint(0, 60)
            tf1 = i + t
            tSistema += t
        elif (formados > 0 and ocupado2 == 0):
            catendidos += 1
            formados -= 1
            ocupado2 = 1
            t = random.randint(0, 60)
            tiempofila2 = i + t
            tSistema += t
        elif (formados > 0 and ocupado3 == 0):
            catendidos += 1
            formados -= 1
            ocupado3 = 1
            t = random.randint(0, 60)
            tiempofila3 = i + t
            tSistema += t

        if (i >= tf1):
            tf1 = 0
            o1 = 0
        if (i >= tiempofila2):
            tiempofila2 = 0
            ocupado2 = 0
        if (i >= tiempofila3):
            tiempofila3 = 0
            ocupado3 = 0


horasProm = (round(float(float(tSistema) / 3600) / iteraciones, 4))
cProm = catendidos / iteraciones

print("Clientes promedio: ", cProm)

print("Horas promedio: ", horasProm)