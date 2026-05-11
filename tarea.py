
import uuid
import datetime

today = datetime.datetime.now()


class Tarea:
    def __init__(nombre, descripcion, categoria, prioridad, estado):
        id = uuid
        nombre = nombre
        descripcion = descripcion
        categoria = categoria
        prioridad = prioridad
        estado = estado
        fecha_creacion = today
        fecha_completado = None

    def completar():
        estado = "completado"
        fecha_completado = today


    def editar(campo, nuevo_valor):
        