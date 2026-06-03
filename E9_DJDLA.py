# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio9 - DJDLA

# Importamos la libreria - DJDLA
import pyfiglet
# Creamos una variable titulo que almacene lo que vamos a mostrar en pantalla - DJDLA
Titulo = pyfiglet.figlet_format("Diego De Leon")
from colorama import init, Fore, Back, Style
init()
print(Fore.LIGHTMAGENTA_EX + Titulo + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX)

# Creamos listas para las temperaturas - DJDLA
Temperaturas = []
for Indice in range(1,6):
    Temperatura = []
    Temperatura.append(int(input("🥵 Dia %d, Temperatura maxima: " % Indice)))
    Temperatura.append(int(input("️🥶 Dia %d, Temperatura minima: " % Indice)))
    Temperaturas.append(Temperatura)

    # Mostrar temperatura media - DJDLA
    print("Temperaturas medias")
    print("=====================")

    Indice = 1
    for Temperatura in Temperaturas:
        print("🌤️ Dia %d, Temperatura media: %f: " % (Indice,sum(Temperatura)/len(Temperatura)))
        Indice += 1

    # Calcular temperatura minima mas pequeña - DJDLA
    # Suponemos que es la primera - DJDLA
    Temp_min = Temperaturas[0][1]
    for Temperatura in Temperaturas:
        if Temperatura[1] < Temp_min:
            Temp_min = Temperatura[1]

    # Mostrar los dias con menos temperatura - DJDLA
    print("🌡️ Dias con menos temperatura")
    print("===========================")
    Indice = 1
    for Temperatura in Temperaturas:
        if Temperatura[1] == Temp_min:
            print("Dia %d" % Indice)
        Indice += 1

    # Dias con temperatura maxima - DJDLA
    Existe_temperatura = False
    print("🌡️ Dias con temperatura maxima")
    print("============================")
    Temp_max = int(input("☀️ Introduce una temperatura:"))
    Indice = 1
    for Temperatura in Temperaturas:
        if Temperatura[0] == Temp_max:
            print("Dia %d" % Indice)
            Existe_temperatura = True
        Indice += 1
    if not Existe_temperatura:
        print("No hay ningun dia con dicha temperatura")