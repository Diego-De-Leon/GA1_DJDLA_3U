# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio8 - DJDLA

# Importamos la libreria - DJDLA
import pyfiglet
# Creamos una variable titulo que almacene lo que vamos a mostrar en pantalla - DJDLA
Titulo = pyfiglet.figlet_format("Diego De Leon")
from colorama import init, Fore, Back, Style
init()
print(Fore.LIGHTMAGENTA_EX + Titulo + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX)

Nombres = []
Edades = []
# Inicializo las listas hasta que introduzca un "*" - DJDLA
while True:
    # Solicitamos nombre de los alumnos - DJDLA
    Nombre = input("👦 Dime el nombre de un alumno: ")
    if Nombre != "*":
        Nombres.append(Nombre)
        # Y tambien solicitamos su edad - DJDLA
        Edades.append(int(input("⏹️ Dime su edad: ")))
    if Nombre == "*": break;

# Calcular la edad maxima - DJDLA
Edad_Max = max(Edades)
# Alumnos mayores de edad - DJDLA
print("Alumnos mayores de edad")
print("========================")
for Nombre,Edad in zip(Nombres,Edades):
    if Edad >= 18:
        print(Nombre)

# Alumnos mayores - DJDLA
print("Alumnos Mayores")
print("================")
for Nombre,Edad in zip(Nombres,Edades):
    if Edad >= Edad_Max:
        print(Nombre)