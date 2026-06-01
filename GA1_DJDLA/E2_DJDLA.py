# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio2 - DJDLA

# Importamos la libreria - DJDLA
import pyfiglet
# Creamos una variable titulo que almacene lo que vamos a mostrar en pantalla - DJDLA
Titulo = pyfiglet.figlet_format("Diego De Leon")
from colorama import init, Fore, Back, Style
init()
print(Fore.LIGHTMAGENTA_EX + Titulo + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX)

# Creamos las listas - DJDLA
Lista1 = []
Lista2 = []
# Recorro la lista1 y leo cada elemento por teclado - DJDLA
for Indice in range(1,6):
    Lista1.append(input("📄 Dame la cadena %d: " % Indice))

# Copio la lista1 en la lista2 en orden inverso - DJDLA
Lista2 = Lista1[::-1]

# Recorro la lista2 para mostrarla - DJDLA
for Cadena in Lista2:
    print(Cadena)