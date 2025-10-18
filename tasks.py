#aqui se estan guardando los datos que el usuario introduce
datos_globales_dicc = []


def agregar_tareas():
    nombre = input("Ingrese el nombre de la tarea.\n")
    categoria = input("Ingrese la categoria de la tarea. \n")
    prioridad = input("Prioridad: Alta / Baja \n")

    while True:
        estado = input("Esta completada la tarea? si/no \n")  #verifica si esta completada o no
        if estado == "si":
            break
        elif estado == "no":
            break
        else:
            print("Porfavor, escriba si o no.")

    nuevo_usuario = {
        "nombre": nombre,
        "categoria": categoria,
        "prioridad": prioridad,
        "estado": estado
    }

    datos_globales_dicc.append(nuevo_usuario)
    print("Tarea ha sido agregada.")


def listar_tareas():
    if not datos_globales_dicc:
        print("No hay datos agregados.")
    else:
        for usuario in datos_globales_dicc:  #en hori muestra los datos guardados.
            print(usuario)


def tareas_completadas():
    if not datos_globales_dicc:
        print("No hay tareas completadas agregadas.")
    else:
        for usuario in datos_globales_dicc:
            if usuario['estado'] == 'si':
                print(usuario)
            else:
                break


def tareas_pendientes():
    for datos in datos_globales_dicc:
        if datos['estado'] == ['no']:
            print(f"Nombre: {datos['nombre']}")
            print(f"Descripcion: {datos['categoria']}")
            print(f"Prioridad: {datos['prioridad']}")
            print(f"Estado: {datos['estado']}")


def filtrar_tareas(datos_guardados):
    pass

#ahora vamos a usar esta nadamas para subir a git y el otro a programar.


# lista_secundaria.append(n_tarea)
# lista_secundaria.append(c_tarea)
# lista_secundaria.append(p_tarea)
# lista_secundaria.append(e_tarea)


# if not lista_tarea:
#     print("No hay datos guardados.")
# else:
#     for indice, (clave, valor) in enumerate(lista_tareas.items()):
#         print(f" {indice + 1}) {clave}: {valor}")      #de esta manera asiganos una llave y lo que el usuario ingrese al momento de imprimir el resultado
#


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
