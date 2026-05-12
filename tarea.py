
import uuid
import datetime

from data import guardar_tareas

#la primera clase con las definiciones desde task.py
class Tarea:
    def __init__(self, nombre, descripcion, categoria, prioridad, estado):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.prioridad = prioridad
        self.estado = estado
        self.fecha_creacion = datetime.datetime.now().strftime("%d/%m/%Y")
        self.fecha_completado = None

    def completar(self):
        self.estado = "completado"
        self.fecha_completado = datetime.datetime.now().strftime("%d/%m/%Y")
    
    #esta basicamente lo convierte a dic para json
    def to_dict(self):
        return {
            "ID": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "prioridad": self.prioridad,
            "estado": self.estado,
            "fecha_creacion": self.fecha_creacion,
            "fecha_completado": self.fecha_completado
        }

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def _lista_para_json(self):
        resultado = []
        for t in self.tareas:
            resultado.append(t.to_dict())
        return resultado
    
    def guardar(self):
        guardar_tareas(self._lista_para_json())
    
    def agregar(self, tarea):
        self.tareas.append(tarea)
        self.guardar()
     
    def listar(self):
        for t in self.tareas:
            print(t.to_dict())
    

    
    
