
def agregar_tareas(lista_tareas):
    nombre_tarea = input("Cual es la tarea que quiere agendar? \n")
    categoria_tarea = input("Cual es la categoria de la tarea? \n")
    prioridad_tarea = input("Agregue la prioridad del 1 - 10 \n")
    estado_tarea = input("Cual es el estado actual de la tarea? \n")
    # Aqui me guarda las tareas en la lista memoria y luego las muestra en listar_tareas
    lista_tareas.append(nombre_tarea)
    lista_tareas.append(categoria_tarea)
    lista_tareas.append(prioridad_tarea)
    lista_tareas.append(estado_tarea)

    print("Tarea agregada con exito")

def tareas_completadas(listar_tareas):
    pass



def listar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas guardadas.")
    else:
        for i, tareas in enumerate(lista_tareas):
            print(f"{i + 1}. {tareas}")



