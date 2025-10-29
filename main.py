

from tasks import agregar_tareas, listar_tareas, tareas_completadas, tareas_pendientes, filtrar_tareas
from utils import cambiar_estado
import sys #exportando funcion para salir del programa

import tasks
3
def mostra_menu():
    print("\n--- Menú Principal ---")
    print("1 - Agregar tareas")
    print("2 - Mostrar las tareas")
    print("3 - Tareas Completadas")
    print("4 - Tareas pendientes")
    print("5 - Filtrar por prioridad")
    print("6 - Cambiar estado de una tarea")
    print("0 - Salir.")


def main():

    tareas_guardadas = []

    while True:
        mostra_menu()
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
        elif opcion == '0':
            print("Saliendo del programa...")
            sys.exit()  #sale del programa



if __name__ == "__main__":
    main()

