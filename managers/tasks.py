import datetime

from utils.utils import validar_inputs, validar_estados

from data.data import guardar_tareas


#aqui se estan guardando los datos que el usuario introduce
# datos_globales_dicc = []

# valor_unico = 0

#fechas que se creo la tarea
ahora = datetime.datetime(2026, 5, 23, 23, 29, 57, 983823)
fecha_formateada = ahora.strftime(" %d/%m/%Y")



#FUNCIONES QUE SE ALIMINARAN DE LA V.1 PORQUE YA ESTAN EN METODOS DE LA CLASE TAREA EN TAREA.PY
#AGREAGR_TAREA, LISTAR_TAREA, TAREAS_COMPLETADAS, TAREA,PENDIENTES, FILTRAR TAREA
#DATOS_GLOBALES_DICC Y VALOR_UNICO ESTOS DOS PORQUE YA NO GUARDAMOS EN LOCAL SINO CON JSON

#info exta
#Funcion principal para agg info del usuario.
# def agregar_tareas():
#     global valor_unico

#     nombre = input("Ingrese el nombre de la tarea.\n")
#     descripcion = input("Ingrese una Descripcion. \n")
#     categoria = input("Ingrese la categoria de la tarea. \n")

#     #esta seccin de prioridad debe de ser eleiminada para hacer la validacion en utils.py
#     while True:
#         prioridad = input("Prioridad: Baja / Media / Alta \n")

#         try:
#             prioridad = validar_inputs(prioridad) #tecnicamente aqui viaja el dato hacia la funcion que los valida.
#             break
#         except ValueError as err:
#             print(f"Incorrecto, intente de nuevo {err}")

        # ESTA ERA LA ENTIGUA FUNCION QUE TENIA, NO LA VOY A ELIMINAR POR SI ACASO QUIERO OPTIMIZAR MAS ADELANTE

        #proridad era string y [] era lista y use mejor el in.
        # if prioridad in ["baja", "media", "alta"]:
        #     break
        # print("Porfavor introduzca una de las opciones.")
        #eliminamos el break mejor mucha paja la vdd 

    #esta seccion de estado debe ser eliminada para hacer la validacioin en utils.py

    # while True:
    #     estado = input("Esta completada la tarea? si/no \n")  #verifica si esta completada o no

    #     try:
    #         estado = validar_estados(estado)
    #         break
    #     except ValueError as e:
    #         print(f"Incorrecto, intente de nuevo {e}")



    #este bucle va aumentando cuando el usuario dice si/no siempre. son los ID asignados.
    #lo vamos a dejar asi aunque ese while se rompe por el break al inicio pero olvidalo funciona.
    # while True:
    #     try:
    #         confirmacion_id = input("Desea usted asignarle un ID unico? \n")
    #         if confirmacion_id == 'si':
    #             res = str(uuid.uuid4())
    #             break
    #         elif confirmacion_id == 'no':
    #             print("Necesitas agregar un ID, agregando...lol\n")
    #             res = str(uuid.uuid4())
    #             break
    #         else:
    #             raise ValueError("Entrada no concedida.\n") #este viene incluido para que pueda aparecer el except.
    #     except ValueError:
    #         print("Introduzca 'si' o 'no' nada mas.")



    # le quitamos el for y los [] arriba a los res = str... porque no encontraba los datos en
    # mis otras funciones, aclaro por si se me olvida.

    #Guarda los inputs al inicio aqui
    # nuevo_usuario = {
    #     "ID": res,
    #     "nombre": nombre,
    #     "descripcion": descripcion,
    #     "categoria": categoria,
    #     "prioridad": prioridad,
    #     "estado": estado,
    #     "fecha_creaacion": fecha_formateada,
    #     "fecha_completado": None
    # }

    # #Junta la info por mientras en una variable global
    # datos_globales_dicc.append(nuevo_usuario)
    # print("Tarea ha sido agregada.")
    # guardar_tareas(datos_globales_dicc)        #de esta manera llamamos a la funcion que guarda los datos OJO



# def confirmarcion_fecha():
#     for pollo in datos_globales_dicc:
#         if pollo['estado'] == 'si'.lower():
#             actualizacion = pollo['estado'] = fecha_formateada
#             datos_globales_dicc.append(actualizacion)
#         elif pollo['estado'] == 'no'.lower():
#             break
            # hasta este punto realmente no se q hacer si el usuario deja no, creo que seria el break por lo mismo no?

#Muestra todas las tareas agregadas.
# def listar_tareas():
#     if not datos_globales_dicc:
#         print("No hay datos agregados.")
#     else:
#         for usuario in datos_globales_dicc:  #en hori muestra los datos guardados.
#             print(usuario)
            


#Muestras las tareas que completaron
# def tareas_completadas():
#     if not datos_globales_dicc:
#         print("No hay tareas completadas agregadas.")
#     else:
#         for usuario in datos_globales_dicc:
#             if usuario['estado'] == 'si':
#                 print(usuario)


#Solamente muestra las que todavia no esta completadas
# def tareas_pendientes():
#     if not datos_globales_dicc:
#         print("No hay tareas pendientes agregadas.")
#     else:
#         for usuario in datos_globales_dicc:
#             if usuario['estado'] == 'no':
#                 print("No hay tareas incompletas.")
#                 print(usuario)
#             else:
#                 continue


#CODIGO HECHO PARA INPO EN EL FUTURO DEL MANEJO DE DATOS.
# def ordenar_tareas():
#     lista_ordenada = sorted(datos_globales_dicc, key=lambda x: 0 if x['prioridad'] == 'alta' else 1)
#     prioridades = {'alta': 0, 'media': 1, 'baja': 2}


#Esta funcion filtra las prioridades
# def filtrar_tareas():
#     #usamos lambda aqui para identificar las q son altas les asignamos 0 y las bajas uno asi iran primero las altas.
#     tarea_ordenadas = sorted(datos_globales_dicc, key=lambda x: 0 if x['prioridad'].lower() == 'alta' else 1)

#     if not tarea_ordenadas:
#         print("No hay datos guardados.")
#         return

#     print("Lista de Tareas")
#     for tarea in tarea_ordenadas:
#         print(f"ID: {tarea['ID']}, Nombre: {tarea['nombre']}, Prioridad: {tarea['prioridad']}")


def editar_tarea(gestor):
    """Edita una tarea usando el gestor"""
    gestor.listar()
    id_tarea = input("ID de la tarea a editar: ")
    tarea = gestor.obtener_por_id(id_tarea)
    
    if not tarea:
        print("No se encontró la tarea.")
        return
    
    print("Campos: nombre, descripcion, categoria, prioridad, estado")
    campo = input("¿Qué campo deseas editar?: ")
    
    if campo in ["nombre", "descripcion", "categoria", "prioridad", "estado"]:
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        gestor.editar(id_tarea, campo, nuevo_valor)
        print("Editado con éxito.")
    else:
        print("Campo no válido.")
