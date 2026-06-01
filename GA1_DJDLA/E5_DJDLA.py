# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio5 - DJDLA

# Importamos la libreria - DJDLA
import pyfiglet
# Creamos una variable titulo que almacene lo que vamos a mostrar en pantalla - DJDLA
Titulo = pyfiglet.figlet_format("Diego De Leon")
from colorama import init, Fore, Back, Style
init()
print(Fore.LIGHTMAGENTA_EX + Titulo + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX)

# Importamos la libreria Random - DJDLA
import random
# Creamos la lista - DJDLA
Lista = []
# Bucle for para recorrer la lista - DJDLA
for Indice in range(1,11):
    Lista.append(random.randint(1,10))
# Ordeno la lista - DJDLA
Lista.sort()

# Recorremos el vector ordenado - DJDLA
for Numero in Lista:
    print(Numero, " ", end="")