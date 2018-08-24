import random

iteraciones = 1000
dinero = 20
num = [4,5,6,8,9,10]
quiebra = 0
gana = 0


def tiro():
    dado1 = int(random.random() * 7)
    dado2 = int(random.random() * 7)
    return dado2+dado1


for i in range(0, iteraciones):

    while dinero < 50 and dinero > 0:

        lock = 0
        sumaDados = tiro()

        if sumaDados == 7 or sumaDados == 11:
            dinero += 1
        elif sumaDados == 2 or sumaDados == 3 or sumaDados == 12:
            dinero -= 1

        if num.__contains__(sumaDados):
            lock = sumaDados

            while sumaDados != 7:
                sumaDados = tiro()
                if sumaDados == lock:
                    dinero += 1
                    break
                elif sumaDados == 7:
                    dinero -= 1
                    break

    if dinero == 50:
        gana += 1
        dinero = 20
    elif dinero == 0:
        quiebra += 1
        dinero = 20

print("El judador se quedo en 0s :",quiebra/iteraciones*100, "% al jugar:", iteraciones, "veces")
print("El jugador llego a mas de $50 :",gana/iteraciones*100,"%al jugar:", iteraciones, "veces")