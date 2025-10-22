#aqui se estan guardando los datos que el usuario introduce
datos_globales_dicc = []

datos_prioridad = []


def agregar_tareas():
    nombre = input("Ingrese el nombre de la tarea.\n")
    categoria = input("Ingrese la categoria de la tarea. \n")

    while True:
        prioridad = input("Prioridad: Alta / Baja \n")
        prioridad.lower()
        if prioridad == ["Alta"] or prioridad == ["Baja"]:
            break
        else:
            print("Porfavor introduzca una de las opciones")
            break

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
    if not datos_globales_dicc:
        print("No hay tareas pendientes agregadas.")
    else:
        for usuario in datos_globales_dicc:
            if usuario['estado'] == 'no':
                print(usuario)
            else:
                continue

def filtrar_tareas():
    if not datos_globales_dicc:
        print("No hay tareas con prioridad agregadas.")
    else:
        for i in datos_globales_dicc:
            if i['prioridad'] == ['Alta', 'alta']:
                print(i)
        for i in datos_globales_dicc:
            if i['prioridad'] == ['Baja', 'baja']:
                print(i)

#revisar el ultimo error hecho en github