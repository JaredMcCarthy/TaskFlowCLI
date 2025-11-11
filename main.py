import os
import sys

from tasks import agregar_tareas, listar_tareas, tareas_completadas, tareas_pendientes, filtrar_tareas
from utils import cambiar_estado, eliminar_tareas
import sys #exportando funcion para salir del programa

import tasks

def logo_inicio():
    logo = r"""
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║   ████████╗ █████╗ ███████╗██╗  ██╗      ║
    ║   ╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝      ║
    ║      ██║   ███████║███████╗█████╔╝       ║
    ║      ██║   ██╔══██║╚════██║██╔═██╗       ║
    ║      ██║   ██║  ██║███████║██║  ██╗      ║
    ║      ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ║
    ║                                          ║
    ║   ███████╗██╗      ██████╗ ██╗    ██╗    ║
    ║   ██╔════╝██║     ██╔═══██╗██║    ██║    ║
    ║   █████╗  ██║     ██║   ██║██║ █╗ ██║    ║
    ║   ██╔══╝  ██║     ██║   ██║██║███╗██║    ║
    ║   ██║     ███████╗╚██████╔╝╚███╔███╔╝    ║
    ║   ╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝     ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
      """
    print(logo)


def limpiar_pantalla():
    """Limpia la pantalla del terminal este codigo"""
    try:
        if os.name == 'nt':  #este es para windows
            os.system('cls')
        else:
            os.system('clear')   #este para mac o linux por si acaso
    except:
        print('\n' * 100)
        #lo use por el try y si falla pues me las imrpime en blanco.

def mostrar_menu():
    limpiar_pantalla()
    logo_inicio()
    print("\n╔════════════════════════════════════╗")
    print("║       --- Menú Principal ---       ║")
    print("╠════════════════════════════════════╣")
    print("║  1 - Agregar tareas                ║")
    print("║  2 - Mostrar las tareas            ║")
    print("║  3 - Tareas Completadas            ║")
    print("║  4 - Tareas pendientes             ║")
    print("║  5 - Filtrar por prioridad         ║")
    print("║  6 - Cambiar estado de una tarea   ║")
    print("║  7 - Eliminar una Tarea            ║")
    print("║  0 - Salir                         ║")
    print("╚════════════════════════════════════╝")
    print()


def main():

    tareas_guardadas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccionar unas de las opciones \n")

        if opcion == '1':
            agregar_tareas()
        elif opcion == '2':
            listar_tareas()
        elif opcion == '3':
            tareas_completadas()
        elif opcion == '4':
            tareas_pendientes()
        elif opcion == '5':
            filtrar_tareas()
        elif opcion == '6':
            cambiar_estado()
        elif opcion == '7':
            eliminar_tareas()
        elif opcion == '0':
            print("Saliendo del programa...")
            sys.exit()  #sale del programa



if __name__ == "__main__":
    main()







