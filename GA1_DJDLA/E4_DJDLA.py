# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio4 - DJDLA

# Importamos la libreria - DJDLA
import pyfiglet
# Creamos una variable titulo que almacene lo que vamos a mostrar en pantalla - DJDLA
Titulo = pyfiglet.figlet_format("Diego De Leon")
from colorama import init, Fore, Back, Style
init()
print(Fore.LIGHTMAGENTA_EX + Titulo + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX)

# Creamos lista para almacenar los numeros ingresados - DJDLA
Lista = []
Numero = int(input("✏️📓 Introduce un numero en la lista: "))
# Bucle while que termina hasta ingresar un numero menor a 0 - DJDLA
while Numero >= 0:
    Lista.append(Numero)
    # Solicitamos el numero al usuario - DJDLA
    Numero = int(input("📘 Introduce un numero en la lista: "))

# Bucle for encargado de mostrar la lista cuando termine el bucle anterior - DJDLA
for Numero in Lista:
    print(Numero, " ", end="")
