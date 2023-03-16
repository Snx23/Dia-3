print("BIENVENITO A LA ISLA DEL TESORO")
print("TU MISION ES ENCONTRAR EL TESORO.")
lab = input("\nA donde quieres ir? \"DERECHA\" O \"IZQUIERDA\"\n").lower()

if lab == "izquierda":
    lago = input("Has venido a un lago. Hay una isla en medio del lago. Escribe \"ESPERA\" para esperar un barco o Escribe \"NADAR\" para cruzar nadando\n").lower()
    if lago == "espera":
        puerta = input("Llegas a la isla ileso. Hay una casa con 3 puertas. Una ROJA, Una AMARILLA y una AZUL. ¿Que color eliges?\n").lower()
        if puerta == "amarilla":
            print("¡Encontraste el tesoro! ¡Tú ganas!")
        elif puerta == "roja":
            print("Es una habitacion llena de fuego. Te has muerto calcinado!!")
        else:
            print("Entraste a la habitacion equivocada. Has sido aplastado por un titan acorazado")
    else:
        print("Te Ataco un COCODRILO. Has Muerto!!")
else:
    print("Caíste en un hoyo. El Juego Termino:(")
