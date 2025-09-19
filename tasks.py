# esta es una lista global
datos_guardados = []


def agregar_tareas(datos_guardados):
    nombre_tarea = input("Cual es la tarea que quiere agendar? \n")
    categoria_tarea = input("Cual es la categoria de la tarea? \n")
    prioridad_tarea = input("Agregue la prioridad del 1 - 10 \n")
    estado_tarea = input("Cual es el estado actual de la tarea? C/N \n")
    datos_guardados.append(nombre_tarea)
    datos_guardados.append(categoria_tarea)
    datos_guardados.append(prioridad_tarea)
    datos_guardados.append(estado_tarea)

    tarea_actual = {
        "Tarea": nombre_tarea,
        "Categoria": categoria_tarea,
        "Prioridad": prioridad_tarea,
        "Estado": estado_tarea
    }

    datos_guardados.append(tarea_actual)

    #este codigo lo dejaremos de backup por si acaso, sigue funcional el otro
    # # Aqui me guarda las tareas en la lista memoria y luego las muestra en listar_tareas
    # lista_tareas.append(nombre_tarea)
    # lista_tareas.append(categoria_tarea)
    # lista_tareas.append(prioridad_tarea)
    # lista_tareas.append(estado_tarea)


def tareas_completadas(listar_tareas):
    pass


def listar_tareas(datos_guardados):
    if not datos_guardados:
        print("No hay datos guardados.")
        return
    else:
        for i, tarea in enumerate(datos_guardados):
            print(f"Tarea #{i + 1}:")
            print(f" Nombre: {tarea['Nombre']}")
            print(f"Categoria: {tarea['Categoria']}")
            print(f"Estado: {tarea['Estado']}")
            print("-" * 20)  #separador visual

    # print("\n--- Estado de las tareas ---")
    # if not datos_guardados:
    #     print("No hay tareas por mostrar.")
    #     return
    # for i, tareas in enumerate(datos_guardados):
    #     print(f"{i + 1}. {tareas}") #me muestra todas las tareas


def filtrar_tareas(datos_guardados):
    for i in range(datos_guardados):
        pass
