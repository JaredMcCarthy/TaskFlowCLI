import os
import platform


from tasks import agregar_tareas, listar_tareas, tareas_completadas, tareas_pendientes, filtrar_tareas, editar_tarea
from utils import cambiar_estado, eliminar_tareas
import sys  #exportando funcion para salir del programa

import tasks


# def logo_inicio():
#     logo = r"""
#     ╔══════════════════════════════════════════╗
#     ║                                          ║
#     ║   ████████╗ █████╗ ███████╗██╗  ██╗      ║
#     ║   ╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝      ║
#     ║      ██║   ███████║███████╗█████╔╝       ║
#     ║      ██║   ██╔══██║╚════██║██╔═██╗       ║
#     ║      ██║   ██║  ██║███████║██║  ██╗      ║
#     ║      ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ║
#     ║                                          ║
#     ║   ███████╗██╗      ██████╗ ██╗    ██╗    ║
#     ║   ██╔════╝██║     ██╔═══██╗██║    ██║    ║
#     ║   █████╗  ██║     ██║   ██║██║ █╗ ██║    ║
#     ║   ██╔══╝  ██║     ██║   ██║██║███╗██║    ║
#     ║   ██║     ███████╗╚██████╔╝╚███╔███╔╝    ║
#     ║   ╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝     ║
#     ║                                          ║
#     ╚══════════════════════════════════════════╝
#       """
#     print(logo)


def limpiar_pantalla():
    if platform.system() == "Windows": #identifica windows
        os.system('cls')
    else:
        os.system('clear') #este identifica linux/mac


def mostrar_menu():
    limpiar_pantalla()
    # logo_inicio()
    print("\n  ╔══════════════════════════════════╗")
    print("  ║       --- Menú Principal ---     ║")
    print("  ╠══════════════════════════════════╣")
    print("  ║  1 - Agregar tareas              ║")
    print("  ║  2 - Mostrar las tareas          ║")
    print("  ║  3 - Tareas Completadas          ║")
    print("  ║  4 - Tareas pendientes           ║")
    print("  ║  5 - Filtrar por prioridad       ║")
    print("  ║  6 - Ir al Menu Avanzado         ║")
    print("  ║  0 - Salir                       ║")
    print("  ╚══════════════════════════════════╝")
    print()


def main():

    while True:
        try:
            mostrar_menu()
            opcion = int(input("Seleccionar unas de las opciones \n"))

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
                menu_2()
            elif opcion == '0':
                print("Saliendo del programa...")
                sys.exit()  #sale del programa
        except ValueError:
            print("Ingrese solamente numeros del 0-6.")


def menu_avanzado():
    limpiar_pantalla()
    print("\n  ╔══════════════════════════════════╗")
    print("  ║       --- Menú Avanzado  ---     ║")
    print("  ╠══════════════════════════════════╣")
    print("  ║  1 - Cambiar Estado de una Tarea ║")
    print("  ║  2 - Eliminar una Tarea          ║")
    print("  ║  3 - Editar una Tarea            ║")
    print("  ║  0 - Regresar al menu Anterior   ║")
    print("  ╚══════════════════════════════════╝")
    print()

def menu_2():
    limpiar_pantalla()
    while True:
        try:
            menu_avanzado()
            opciones2 = int(input("Seleccione una de las opciones.\n"))

            if opciones2 == '1':
                cambiar_estado()
            elif opciones2 == '2':
                eliminar_tareas()
            elif opciones2 == '3':
                editar_tarea()
            elif opciones2 == '0':
                break
        except ValueError:
            print("Ingrese solamente un numero del 0-3")


if __name__ == "__main__":
    main()
