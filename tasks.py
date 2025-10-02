# esta es una lista global pero diccionario
datos_guardados = {}
# lista_secundaria = []   #para ver si muestro algo de completados esos datos
#solo por si acaso mejor eliminemos eso y dejemos una lista global por si acaso

def agregar_tareas(datos_guardados):
    nombre = input("Inserte el nombre de su tarea.")
    categoria = input("Inserte el categoria de su tarea.")


def tareas_completadas(t_completado):
        global tareas_hechas
        r_competada = input("Quieres ver todas las tareas completadas? S/N\n")

        if r_competada == 'S':
            tareas_completadas(t_completado)

            tareas_hechas = (tarea for tarea in datos_guardados if tarea['estado'] == 'C')

        if not tareas_hechas:
            print("No hay tareas completadas.")
            return
        for i, tarea in enumerate(tareas_hechas, 1):
            print(f"{i}, {tarea['Tarea']} - Categoria: {tarea['Categoria']} - Prioridad: {tarea['prioridad']} - Estado: {tarea['estado']}")


def listar_tareas(datos_guardados):
    if not datos_guardados:
        print("No hay datos guardados.")
    else:
        for indice, (clave, valor) in enumerate(datos_guardados.items()):
            print(f" {indice + 1}) {clave}: {valor}")      #de esta manera asiganos una llave y lo que el usuario ingrese al momento de imprimir el resultado



def filtrar_tareas(datos_guardados):
    for i in range(datos_guardados):
        pass

    # lista_secundaria.append(n_tarea)
    # lista_secundaria.append(c_tarea)
    # lista_secundaria.append(p_tarea)
    # lista_secundaria.append(e_tarea)



    # nombre_tarea = input("Cual es la tarea que quiere agendar? \n")
    # categoria_tarea = input("Cual es la categoria de la tarea? \n")
    # prioridad_tarea = input("Agregue la prioridad del 1 - 10 \n")
    # estado_tarea = input("Cual es el estado actual de la tarea? C/N \n")
    # datos_guardados.append(nombre_tarea)
    # datos_guardados.append(categoria_tarea)
    # datos_guardados.append(prioridad_tarea)
    # datos_guardados.append(estado_tarea)

    # tarea_actual = {
    #     datos_guardados['Tarea'] =  nombre_tarea,
    #     "Categoria": categoria_tarea,
    #     "Prioridad": prioridad_tarea,
    #     "Estado": estado_tarea
    # }

    # datos_guardados.append(tarea_actual)

    #este codigo lo dejaremos de backup por si acaso, sigue funcional el otro
    # # Aqui me guarda las tareas en la lista memoria y luego las muestra en listar_tareas
    # lista_tareas.append(nombre_tarea)
    # lista_tareas.append(categoria_tarea)
    # lista_tareas.append(prioridad_tarea)
    # lista_tareas.append(estado_tarea)

            # print(f" Nombre: {tarea['Tarea']}")
            # print(f"Categoria: {tarea['Categoria']}")
            # print(f"Estado: {tarea['Estado']}")
            # print("-" * 20)  #separador visual

    # print("\n--- Estado de las tareas ---")
    # if not datos_guardados:
    #     print("No hay tareas por mostrar.")
    #     return
    # for i, tareas in enumerate(datos_guardados):
    #     print(f"{i + 1}. {tareas}") #me muestra todas las tareas


