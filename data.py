#LOGRAR QUE LOS DATOS SE GUARDEN PERMANENTEMENTE

#estas son lib para guardar, cargar y tener backups
#uno de tiempo por si necesitamos registrar hora de guardado
import json
import pathlib
import shutil
import datetime

#esta funcion llena la mochila por decirlo asi
def guardar_tareas(lista_tareas):
    with open('datos_globales_dicc.json', 'w', encoding='utf-8') as f:
        json.dump(lista_tareas, f, indent=4)
    print("Tareas guardadas exitosamente.")

#PARA QUE NUNCA SE NOS OLVIDE O ALMENOS RECORDEMOS
# HACEMOS LA FUNCION PRIMERO Y DE PARAMETRO METEMOS LA LISTA DONDE SE GUARDAN
# ABRIMOS EL ARCHIVO Y ESE ES LA LISTA DE DATOS GLOBALES CON JSON, EN W Y ENCODING COMO F DECLARAMOS
#LUEGO USAMOS DUMP O LOAD PARA CARGAR LOS DATOS DENTRO DE LISTA TAREAS CON IDENT Y F
#Y ABRIMOS NADA MAS.


#esta funcion saca las cosas de la mochila por decirlo asi
def cargar_tareas():
    try:
        with open("datos_globales_dicc.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print("Archivo no encontrado :(")
        return []
#IGUALMENTE PARA CARGAR ARCHIVOS AL JSON Y MOSTRARLOS
# AQUI HAY UN TRY
# INTENTA ABRIUEL EL ARCHIVO MISMO QUE AL ENTERIOR, CON R DE READ Y ENCODING COMO ARCHIVO
# MOSTRAMOS LOS DATOS EN UNA VARIABLE DATOS CON JSON Y USAMOS LOAD PARA CARGAR A ARCHIVOS
# Y REGRESAMOS LOS DATOS QUE CARGO AL ARCHIVO
#LO DEMAS ES EXCEPT YA SABES.