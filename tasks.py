
import random

tareas = []
random_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_letter = ["A", "E", "I", "O", "U"]

def agregar_tareas(tarea):
    tareas.append(tareas)
    print(f"La tarea {tarea} se agrego a la lista.")
    print(f"La categoria {nueva_categoria} se agrego a la lista.")

def tareas_completadas():
    print("Que tareas estan completas?")
    print("Inserte el codigo de tarea")   #aqui la logica hay que trabajarla para que cuando el usuario quiera senalar que esta completa, se marque completa
                                        #y luego se marque como completa en la lista global o crear otra no se.

def listar_tareas():
    if not tareas:
        print("No ha sido agregada a la lista.")
    else:
        print("-----Lista de tareas-----")
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea}")
            break



# import main
#
#
# # import main
#
#
# # guarder las tareas en una lista global por hora
# #crear la funcion agragr tareas DONE
#
#
# def agregar_tareas():
#     global lista_global
#
#
# def listar_tareas():
#     pass
