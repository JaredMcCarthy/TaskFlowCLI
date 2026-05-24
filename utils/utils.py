import datetime

# No importar `tasks` al cargar este archivo: si `tasks` también importa `utils`,
# Python no termina de inicializar `tasks` y sale ImportError (import circular).
# Los imports de `tasks` van dentro de las funciones que los necesitan.

time = datetime.datetime.now()
hora_completed = time.strftime("%H:%M:%S")

# ANTES DE ESCRIBIR CODIGO EN ESTE ARCHIVO PIENSA:
# Y TMB DECILO EN VOS ALTA JARED

# QUE TIPO DE DATO ESTOY ITERANDO? 
# ESTOY ACCEDIENDO POR INDICE O POR CLAVE?

# RECORDA EL DOLOR DE HUEVOS QUE FUE HACER ESTAS DOS FUNCIONES DE ABAJO LOL


#FUNCION ELIMINADA PORQUE LA PASAMOS A tarea.py PORQUE YA NO USA LA LISTA GLOBAL EN LA V.1

# def cambiar_estado():
#     from managers.tasks import datos_globales_dicc, listar_tareas
#     from data.data import guardar_tareas

#     confirmacion = input("Desea cambiar el estado de una tarea? \n")

#     listar_tareas()
#     req_id = input("Ingrese el numero de tarea que quiere cambiar \n")
#     encontrado = False

#     #lo mejor seria recorrer por el elemento directamente
#     for tarea in datos_globales_dicc:
#         if tarea['ID'] == req_id:
#             encontrado = True
#             if tarea['estado'] == 'si':
#                 tarea['estado'] = 'no'
#             else:
#                 tarea['estado'] = 'si'
#             print('Estado cambiado con exito.')
#             guardar_tareas(datos_globales_dicc)
#             break
#     if not encontrado:
#         print("No se encontro la tarea.")


# FUNCIONA ELIMINADA Y PUESTA EN tarea.py PORQUE USABA LA LISTA GLOBAL DE V.1
#USAN EL SISTEMA VIEJO ANTES DE PONERLO EN POO

# def eliminar_tareas():
#     from managers.tasks import datos_globales_dicc, listar_tareas
#     from data.data import guardar_tareas

#     listar_tareas()
#     req_id2 = input('Ingrese el numero de tarea que quiere eliminar\n') #problema en el int
#     encontrado2 = False

#     for tarea2 in datos_globales_dicc:
#         if tarea2['ID'] == req_id2:
#             encontrado2 = True
#             datos_globales_dicc.remove(tarea2)  #mejor porque ya se el ID
#             print("Tarea eliminada con exito.")
#             guardar_tareas(datos_globales_dicc)
#             break
#     if not encontrado2:
#         print("No hay ningun numero con esa tarea.")


# se quedan estas dos porque se necesitan en main.py para validar

def validar_inputs(info_del_user):
    normalizado = info_del_user.strip().lower()

    if normalizado not in {"baja", "media", "alta"}:
        raise ValueError("Ingresá solo: Baja, Media o Alta.")

    return normalizado

def validar_estados(dato_usuario):
    revision = dato_usuario.strip().lower()

    if revision not in {"si", "no"}:
        raise ValueError("Ingresa solo: No o Si")
