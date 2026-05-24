import os
import platform

from models.tarea import Tarea, GestorTareas
from data.data import cargar_tareas, guardar_tareas


from managers.tasks import editar_tarea
import sys


#esta es una variable global
gestor = None

# TOMA DEMASIADO ESPACIO EL LOGO POR ESO MEJOR LO QUITE 
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

#cambiamos la carga de datos de main por este que queda mejor por las clases que importamos
def main():
    global gestor
    gestor = GestorTareas()
    tareas_dict = cargar_tareas()
    for tarea_data in tareas_dict:
        t = Tarea(
            nombre=tarea_data['nombre'],
            descripcion=tarea_data['descripcion'],
            categoria=tarea_data['categoria'],
            prioridad=tarea_data['prioridad'],
            estado=tarea_data['estado']
        )
        gestor.tareas.append(t)

    while True:
        try:
            mostrar_menu()
            opcion = int(input("Seleccionar unas de las opciones \n"))

            if opcion == 1:
                nombre = input("Nombre de la tarea: ")
                descripcion = input("Descripcion: ")
                categoria = input("Categoria: ")
                prioridad = input("Prioridad (alta/media/baja): ")
                estado = input("Estado (si/no): ")

                tarea_nueva = Tarea(
                    nombre=nombre,
                    descripcion=descripcion,
                    categoria=categoria,
                    prioridad=prioridad,
                    estado=estado
                )
                gestor.agregar(tarea_nueva)

            elif opcion == 2:
                gestor.listar()
            elif opcion == 3:
                gestor.listar_completadas()
            elif opcion == 4:
                gestor.listar_pendientes()
            elif opcion == 5:
                prioridad = input("Prioridad a filtrar (alta/media/baja)")
                tareas = gestor.filtrar_por_prioridad(prioridad)
                for tarea in tareas:
                    print(tarea.to_dict())
            elif opcion == 6:
                menu_2()
            elif opcion == 0:
                print("Saliendo del programa...")
                sys.exit()  #sale del programa
            else:
                print("Opcione no valida!")
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

            if opciones2 == 1:
                gestor.listar()
                id_tarea = input("ID de la tarea: ")
                if gestor.cambiar_estado(id_tarea):
                    print("Estado cambiado.")
                else:
                    print("No encontrada.")
            elif opciones2 == 2:
                gestor.listar()
                id_tarea = input("ID de la tarea a eliminar: ")
                if gestor.eliminar(id_tarea):
                    print("Eliminada.")
                else:
                    print("No encontrada.")
            elif opciones2 == 3:
                editar_tarea(gestor)
            elif opciones2 == 0:
                break
            else:
                print("Opcion no valida!")
        except ValueError:
            print("Ingrese solamente un numero del 0-3")


if __name__ == "__main__":
    main()