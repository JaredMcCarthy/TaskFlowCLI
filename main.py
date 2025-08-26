
from tasks import agregar_tareas, listar_tareas, tareas_completadas
import sys

def mostrar_menu():
    print("\n--- Menú ---")
    print("1 - Agregar una tarea nueva")
    print("2 - Mostrar las tareas guardadas")
    print("3 - Salir del programa.")


def submenu_tareas():
    print("1 - Ver todas las tareas.")
    print("2 - Ver las tareas compledas")
    print("3 - Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion \n")

    if opcion == '1':
        nueva_tarea = input("Agregue una nueva tarea.\n")
        nueva_categoria = input("Agregue la categoria.\n")
        nueva_prioridad = input("Agregue la prioridad.\n")
        nuevo_estado = input("Agregue el estado de la tarea.\n")
        agregar_tareas(nueva_tarea)
        agregar_tareas(nueva_categoria)
        agregar_tareas(nueva_prioridad)
        agregar_tareas(nuevo_estado)

    elif opcion == '2':
        submenu_tareas()
        while True:
            subopt = input("Seleccione una de las opciones.\n")
            if subopt == '1':
                listar_tareas()
            elif subopt == '2':
                tareas_completadas()
            else:
                print("Saliendo del sistema")
                sys.exit()
            break


    elif opcion == '3':
        print("Saliendo del programa con exito ;)")
        sys.exit()
    break






































#
# hacer un menu para probar anandir tareas
# # el objetivo es que el programa me deje agregar tareas y que se guarde en una lista de memoria
#
#
# lista_global = []
#
#
# class clase_principal:
#     def __init__(self, tarea, category, prioridad, estado):
#         self.tarea = tarea
#         self.category = category
#         self.prioridad = prioridad
#         self.estado = estado
#
#
# def menu_inicio():
#     while True:
#         print("\n--- Menú ---")
#         print("1 - Agregar una tarea nueva")
#         print("2 - Mostrar las tareas guardadas")
#
#         opcion = input("Porfavor seleccione una opcion.\n")
#         try:
#             if opcion == '1':
#                 tarea = input("Ingrese el nombre de la tarea.\n")
#                 category = input("Ingrese la categoria la categoria\n")
#                 prioridad = input("Ingrese la prioridad de la tarea.\n")
#                 estado = input("Ingrese el estado actual.\n")
#                 confirmacion = input("Desea confirmar las tareas? S/N\n")
#
#                 if confirmacion == "S":
#                     objeto = clase_principal(tarea, category, prioridad, estado)
#                     lista_global.append(objeto)
#                     print("Los datos se han agreagdo a la lista.")
#                     break
#
#                 if confirmacion == '2':
#                         print( {
#                             "Nombre": f"{obj.tarea}",
#                             "Categoria": f"{obj.category}",
#                             "Prioridad": f"{obj.prioridad}",
#                             "Estado:": f"{obj.estado}",
#                             })
#
#
#         except ValueError:
#             print("Ingresa valores que sean aceptados.")
#             break
#
#
# menu_inicio()
#
# for obj in lista_global:
#     print(f"Tarea: {obj.tarea}, Categotia: {obj.category}, prioridad: {obj.prioridad}, estado: {obj.estado}.")
#
