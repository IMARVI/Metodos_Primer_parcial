import numpy,random

inversion = numpy.random.triangular(-130000,-100000,-80000)
rescate = numpy.random.triangular(16000,20000,26000)
infacion = numpy.random.triangular(15,20,25)

flujos = 0

anios= []

for x in range(0,5):
    r = random.random()
    if r < 0.2:
        flujos+= 20000
        anios.append(20000)
    elif r >= 0.2 and r < 0.4:
        flujos+= 30000
        anios.append(30000)
    elif r >= 0.4 and r < 0.6:
        flujos+= 40000
        anios.append(40000)
    elif r >= 0.6 and r < 0.8:
        flujos+= 50000
        anios.append(50000)
    else:
        flujos+= 60000
        anios.append(60000)


npv = numpy.npv(infacion,anios)

impuestos = npv*0.5
trema = npv*0.2

print(f"El VPN es ${npv} la inversion es -${inversion}")
print("Quintando impuestos y sumando el rescate:")
npv -= impuestos 
npv -= trema
npv += rescate
print(npv)

if npv > inversion:
    print("No es conveniente")
else:
    print("Es conveniente")