# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio1 - DJDLA

# Importamos la libreria - DJDLA
import pyfiglet
# Creamos una variable titulo que almacene lo que vamos a mostrar en pantalla - DJDLA
Titulo = pyfiglet.figlet_format("Diego De Leon")
from colorama import init, Fore, Back, Style
init()
print(Fore.LIGHTMAGENTA_EX + Titulo + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX)

print("🧮 Numeros aleatorios: ")
# Importamos libreria Random para generar numeros aleatorios - DJDLA
import random
Lista_Numeros = []
# Primer recorrido para leer la lista - DJDLA
for indice in range(1,11):
    Lista_Numeros.append(random.randint(1,10))
    # Segundo recorrido para mostrar el resultado - DJDLA
for Numero in Lista_Numeros:
    print(Numero, " ", Numero ** 2, " ",Numero ** 3 )