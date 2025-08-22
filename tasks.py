

tareas = []

def agregar_tareas(tarea):
    tareas.append(tareas)
    print(f"La tarea {tarea} se agrego a la lista.")


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
