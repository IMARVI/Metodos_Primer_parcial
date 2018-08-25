import random

iteraciones = 5000

jugador1 = 200
jugador2 = 200

apuestaJugador2 = 1
apuestaMax = False


def ruleta():
    numero = int(random.random() * 23)
    if numero < 10:
        return 1 #color Negro
    elif numero >= 10 and numero < 20:
        return 2 #Color Rojo
    else:
        return 0 #Color Verde


for i in range(0, iteraciones):

    tiro = ruleta()

    if tiro == 2:  # ganan
        jugador1 += 1
        jugador2 += apuestaJugador2

    elif tiro == 1:  # pierden
        jugador1 -= 1
        jugador2 -= apuestaJugador2
        apuestaJugador2 *= 2

        if apuestaJugador2 > 500 and not apuestaMax:
            apuestaJugador2 = 500
            apuestaMax = not apuestaMax
        elif apuestaJugador2 > 500 and apuestaMax:
            apuestaJugador2 = 1
            apuestaMax = not apuestaMax

    else:  # tiro verde
        while tiro == 0:
            tiro = ruleta()
            if tiro == 1:  # pierden
                jugador1 -= 1
                jugador2 -= apuestaJugador2
                apuestaJugador2 *= 2

                if apuestaJugador2 > 500 and not apuestaMax:
                    apuestaJugador2 = 500
                    apuestaMax = not apuestaMax
                elif apuestaJugador2 > 500 and apuestaMax:
                    apuestaJugador2 = 1
                    apuestaMax = not apuestaMax


print("Saldo del Jugador 1 al jugar 5000 veces",jugador1)
print("Saldo del Jugador 2 al jugar 5000 veces",jugador2)