
#aqui se estan guardando los datos que el usuario introduce
datos_globales_dicc = []



#Funcion principal para agg info del usuario.
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

    #Guarda los inputs al inicio aqui
    nuevo_usuario = {
        "nombre": nombre,
        "categoria": categoria,
        "prioridad": prioridad,
        "estado": estado
    }


    #Junta la info por mientras en una variable global
    datos_globales_dicc.append(nuevo_usuario)
    print("Tarea ha sido agregada.")



#Muestra todas las tareas agregadas.
def listar_tareas():
    if not datos_globales_dicc:
        print("No hay datos agregados.")
    else:
        for usuario in datos_globales_dicc:  #en hori muestra los datos guardados.
            print(usuario)


#Muestras las tareas que completaron
def tareas_completadas():
    if not datos_globales_dicc:
        print("No hay tareas completadas agregadas.")
    else:
        for usuario in datos_globales_dicc:
            if usuario['estado'] == 'si':
                print(usuario)
            else:
                break


#Solamente muestra las que todavia no esta completadas
def tareas_pendientes():
    if not datos_globales_dicc:
        print("No hay tareas pendientes agregadas.")
    else:
        for usuario in datos_globales_dicc:
            if usuario['estado'] == 'no':
                print(usuario)
            else:
                continue


#Esta funcion filtra las prioridades
def filtrar_tareas():
    if not datos_globales_dicc:
        print("No hay datos guardados por el momento.")
    else:
        for tarea, i in datos_globales_dicc:
            print(f"{i}, Nombre: {tarea['nombre']}, Tipo: {tarea['prioridad']}")



def cambiar_estado():
    while True:
        confirmacion = input("Desea cambiar el estado de una tarea? ")

        if confirmacion  == 'no':
            confirmacion = False
            print("Regresando a inicio")
            break
        else:
            pass











