# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio7 - DJDLA

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
Lista3 = []

for Indice in range(1,6):
    # Solicitamos al usuario que ingrese un elemento a la lista - DJDLA
    Lista1.append(int(input("✅ Introduce el elemento %d de la lista1: " % Indice)))
for Indice in range(1,6):
    # Solicitamos al usuario que ingrese un elemento a la lista - DJDLA
    Lista2.append(int(input("✅ Introduce el elemento %d de la lista2: " % Indice)))

for Indice in range(0,5):
    Lista3.append(Lista1[Indice] + Lista2[Indice])

# Mostramos la suma total de las listas - DJDLA
print("🧮 La suma de las listas es de: ")
for Numero in Lista3:
    print(Numero, " ", end="")