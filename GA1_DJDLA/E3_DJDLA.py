# GA1 - DJDLA
# Diego José De León Alvarado
# Ejercicio3 - DJDLA

# Importamos la libreria - DJDLA
import pyfiglet
# Creamos una variable titulo que almacene lo que vamos a mostrar en pantalla - DJDLA
Titulo = pyfiglet.figlet_format("Diego De Leon")
from colorama import init, Fore, Back, Style
init()
print(Fore.LIGHTMAGENTA_EX + Titulo + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX)

# Creamos lista para almacenar las notas ingresadas - DJDLA
Notas = []
# Bucle for para permitir ingresar varias notas a la lista - DJDLA
for Indice in range(1,6):
    while True:
        # Solicitamos la nota al usuario - DJDLA
        Nota = int(input("📝 Introduce la nota %d: " % Indice))
        if Nota >=0 and Nota<=100: break
    Notas.append(Nota)

# Mostramos resultados - DJDLA
print("Notas: ", end="")
for Nota in Notas:
    print(Nota, " ", end="")
print()
# Promedio de notas - DJDLA
print("☑️ Nota media: ", sum(Notas)/len(Notas))
# Nota maxima - DJDLA
print("✅ Nota maxima: ", max(Notas))
# Nota minima - DJDLA
print("❌ Nota minima: ", min(Notas))
