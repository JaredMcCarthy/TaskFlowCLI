import datetime
import uuid

#aqui se estan guardando los datos que el usuario introduce
datos_globales_dicc = []

valor_unico = 0

#fechas que se creo la tarea
ahora = datetime.datetime.now()
fecha_formateada = ahora.strftime("%d/%m/%Y")


#info exta
#Funcion principal para agg info del usuario.
def agregar_tareas():
    global valor_unico

    nombre = input("Ingrese el nombre de la tarea.\n")
    descripcion = input("Ingrese una Descripcion. \n")
    categoria = input("Ingrese la categoria de la tarea. \n")

    while True:
        prioridad = input("Prioridad: Alta / Baja \n").lower()
        #proridad era string y [] era lista y use mejor el in.
        if prioridad in ["alta", "baja"]:
            break
        print("Porfavor introduzca una de las opciones.")
        #eliminamos el break mejor mucha paja la vdd

    while True:
        estado = input("Esta completada la tarea? si/no \n")  #verifica si esta completada o no
        if estado == "si":
            break
        elif estado == "no":
            break
        else:
            print("Porfavor escriba Si o no.")


    #este bucle va aumentando cuando el usuario dice si/no siempre. son los ID asignados.
    #lo vamos a dejar asi aunque ese while se rompe por el break al inicio pero olvidalo funciona.
    while True:
        try:
            confirmacion_id = input("Desea usted asignarle un ID unico? \n")
            if confirmacion_id == 'si':
                res = str(uuid.uuid4())
                break
            elif confirmacion_id == 'no':
                print("Necesitas agregar un ID, agregando...lol\n")
                res = str(uuid.uuid4())
                break
            else:
                raise ValueError("Entrada no concedida.\n") #este viene incluido para que pueda aparecer el except.
        except ValueError:
            print("Introduzca 'si' o 'no' nada mas.")



    # le quitamos el for y los [] arriba a los res = str... porque no encontraba los datos en
    # mis otras funciones, aclaro por si se me olvida.

    #Guarda los inputs al inicio aqui
    nuevo_usuario = {
        "ID": res,
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "estado": estado,
        "fecha_creaacion": fecha_formateada,
        "fecha_completado": None
    }

    #Junta la info por mientras en una variable global
    datos_globales_dicc.append(nuevo_usuario)
    print("Tarea ha sido agregada.")


def confirmarcion_fecha():
    for pollo in datos_globales_dicc:
        if pollo['estado'] == 'si'.lower():
            actualizacion = pollo['estado'] = fecha_formateada
            datos_globales_dicc.append(actualizacion)
        elif pollo['estado'] == 'no'.lower():
            break
            # hasta este punto realmente no se q hacer si el usuario deja no, creo que seria el break por lo mismo no?

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


#CODIGO HECHO PARA INPO EN EL FUTURO DEL MANEJO DE DATOS.
# def ordenar_tareas():
#     lista_ordenada = sorted(datos_globales_dicc, key=lambda x: 0 if x['prioridad'] == 'alta' else 1)
#     prioridades = {'alta': 0, 'media': 1, 'baja': 2}


#Esta funcion filtra las prioridades
def filtrar_tareas():
    #usamos lambda aqui para identificar las q son altas les asignamos 0 y las bajas uno asi iran primero las altas.
    tarea_ordenadas = sorted(datos_globales_dicc, key=lambda x: 0 if x['prioridad'].lower() == 'alta' else 1)

    if not tarea_ordenadas:
        print("No hay datos guardados.")
        return

    print("Lista de Tareas")
    for tarea in tarea_ordenadas:
        print(f"ID: {tarea['ID']}, Nombre: {tarea['nombre']}, Prioridad: {tarea['prioridad']}")


def editar_tarea():
    listar_tareas()
    n = input("Ingrese el ID de la tarea que desea editar\n")
    encontrado = False

    for credencial in datos_globales_dicc:
        if credencial['ID'] == n:
            encontrado = True
            print("Escribe el campo en minuscula sin espacion ni signos.")
            edicion = input("Introduzca el area que quiere editar de la tarea. \n")
            #no recorrer otra vez porque solo lo haces una vez arriba cuando buscas el ID basicamente
            #tene en cuenta esta funcion pq creo que nos puede servir para despues
            if edicion == "nombre":
                nom_edicion = input("Que nombre quiere ponerle a su tarea? \n ")
                credencial['nombre'] = nom_edicion
                print("Campo editado con exito!")

            elif edicion == "descripcion":
                des_edicion = input("Que descripcion quiere agregarle? \n")
                credencial['descripcion'] = des_edicion
                print("Descripcion editada con exito!")

            elif edicion == "categoria":
                ca_edicion = input("Que categoria quiere ponerle a su tarea? ")
                credencial['categoria'] = ca_edicion
                print("Categoria editada con exito!")

    if not encontrado:
        print("No se encontro la tarea.")


# Para cuando regreses seria bueno que el campo de fecha_compleado cambiara cuando el usuario
# desee editar el estado, si el estado al crear la tarea es 'Si' pone esa fecha pero si lo edita
# entonces que quite la fecha pero cuando edite la fecha de compleado cambie a ese dia.

#aqui mismo en esta funcion de arriba.
