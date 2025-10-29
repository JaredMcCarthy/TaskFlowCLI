 
import random

#aqui se estan guardando los datos que el usuario introduce
datos_globales_dicc = []

valor_unico = 0



#Funcion principal para agg info del usuario.
def agregar_tareas():
    global valor_unico
    nombre = input("Ingrese el nombre de la tarea.\n")
    categoria = input("Ingrese la categoria de la tarea. \n")

    while True:
        prioridad = input("Prioridad: Alta / Baja \n")
        prioridad.lower()
        #proridad era string y [] era lista y use mejor el in.
        if prioridad.lower() in ["alta", "baja"]:  
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

    #este bucle va aumentando cuando el usuario dice si/no siempre. son los ID asignados.
    #lo vamos a dejar asi aunque ese while se rompe por el break al inicio pero olvidalo funciona.
    while True:
        confirmacion_id = input("Desea usted asignarle un ID unico? \n")
        if confirmacion_id == 'si':
            valor_unico = valor_unico + 1
            break
        elif confirmacion_id == 'no':
            print("Necesitas agregar un ID, agregando...lol")
            valor_unico = valor_unico + 1
            break


    #Guarda los inputs al inicio aqui
    nuevo_usuario = {
        "ID": valor_unico,
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
        for tarea in datos_globales_dicc:
            print(f"ID: {tarea['ID']} , Nombre: {tarea['nombre']}, Tipo: {tarea['prioridad']}")






























