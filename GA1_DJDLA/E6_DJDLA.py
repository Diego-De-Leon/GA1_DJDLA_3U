# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio6 - DJDLA

# Importamos la libreria - DJDLA
import pyfiglet
# Creamos una variable titulo que almacene lo que vamos a mostrar en pantalla - DJDLA
Titulo = pyfiglet.figlet_format("Diego De Leon")
from colorama import init, Fore, Back, Style
init()
print(Fore.LIGHTMAGENTA_EX + Titulo + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX)

# Creamos la lista para los dias de los meses - DJDLA
Dias = [31,28,31,30,31,30,31,31,30,31,30,31]
# Creamos la lista para los meses del año - DJDLA
Nombre_Mes = ["Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Bucle while true para Recorrer las listas y encontrar el mes y la cantidad de dias - DJDLA
while True:
    Mes = int(input("📆📅 Introduce un mes (1-12): "))
    if Mes < 1 or Mes > 12:
        print("Error: Mes incorrecto. ")
    if Mes >= 1 and Mes <= 12: break
    # Mostramos el mensaje final - DJDLA
print("📆 El mes de", Nombre_Mes[Mes-1], "tiene", Dias[Mes-1], "dias.")