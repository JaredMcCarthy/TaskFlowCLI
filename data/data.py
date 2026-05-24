import datetime
import json
import shutil
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "datos_globales_dicc.json"
BACKUP_DIR = Path(__file__).resolve().parent / "backups"



#seccion unicamente para backups de datos subidos
def hacer_backup():
    """
    Crea una copia de seguridad del JSON actual (si existe).
    """
    if not DATA_PATH.exists():
        return

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"datos_globales_dicc_{timestamp}.json"
    shutil.copy2(DATA_PATH, backup_path)

#hasta aqui termino la funcion de backups de los datos json


def guardar_tareas(lista_tareas):
    # Backup automático antes de sobrescribir el archivo principal
    hacer_backup()

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(lista_tareas, f, indent=4, ensure_ascii=False)

#PARA QUE NUNCA SE NOS OLVIDE O ALMENOS RECORDEMOS
# HACEMOS LA FUNCION PRIMERO Y DE PARAMETRO METEMOS LA LISTA DONDE SE GUARDAN
# ABRIMOS EL ARCHIVO Y ESE ES LA LISTA DE DATOS GLOBALES CON JSON, EN W Y ENCODING COMO F DECLARAMOS
#LUEGO USAMOS DUMP O LOAD PARA CARGAR LOS DATOS DENTRO DE LISTA TAREAS CON IDENT Y F
#Y ABRIMOS NADA MAS.


#esta funcion saca las cosas de la mochila por decirlo asi

def cargar_tareas():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            if not datos:
                return [] 
        return datos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("El archivo de tareas está corrupto. Se iniciará con una lista vacía.")
        return []

#IGUALMENTE PARA CARGAR ARCHIVOS AL JSON Y MOSTRARLOS
# AQUI HAY UN TRY
# INTENTA ABRIUEL EL ARCHIVO MISMO QUE AL ENTERIOR, CON R DE READ Y ENCODING COMO ARCHIVO
# MOSTRAMOS LOS DATOS EN UNA VARIABLE DATOS CON JSON Y USAMOS LOAD PARA CARGAR A ARCHIVOS
# Y REGRESAMOS LOS DATOS QUE CARGO AL ARCHIVO
#LO DEMAS ES EXCEPT YA SABES.

#NOTA IMPORTANTE PARA QUE NO LO OLVIDES WEY
# EL ARCHIVO OFICIAL QUE USAMOS ES DATOS_GLOBALES_DICC.JSON