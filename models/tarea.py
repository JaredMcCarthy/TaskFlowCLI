
import uuid
import datetime

from data.data import guardar_tareas

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

    def editar(self, campo, nuevo_valor): 
        if hasattr(self, campo): #si no existe lo reemplaza por el nuevo valor
            setattr(self, campo, nuevo_valor)
        else:
            raise ValueError(f"El campo {campo} ya existe.") #si no pues solo dice usando raise 



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
    
    def agregar(self, tarea):  #aqui ojo porque guardamos las tareas en la lista, este es un metodo de la clase que igual llamamos en main al momento de guardar tareas
        self.tareas.append(tarea)
        self.guardar()
     
    def listar(self):
        for t in self.tareas:
            print(t.to_dict())
    
    def listar_completadas(self):
        if not self.tareas:
            print("No hay tareas completadas agregadas.")
        else:
            for tarea in self.tareas:
                if tarea.estado == 'si':
                    print(tarea.to_dict())

    def listar_pendientes(self):
        if not self.tareas:
            print("No hay tareas pendientes agregadas.")
        else:
            for tarea in self.tareas:
                if tarea.estado == 'no':
                    print(tarea.to_dict())
    
    #de aqui se empieza la tarea 2 basicamente
    
    def filtrar_por_prioridad(self, prioridad):
        #aqui devuelve las tareas de esa prioridad osea las que tiene esa prioridad que se seleccionan
        resultado = []
        for t in self.tareas:
            if t.prioridad.lower() == prioridad.lower(): #se recorre como siempre la tareas porque ahi se guardan los datos y se comparan
                resultado.append(t)
        return resultado
    
    def obtener_por_id(self, id_tarea):
        #buscar por id la tarea, las tareas estan dentro de tareas la variable por eso recorre por ahi el for
        for t in self.tareas:
            if t.id == id_tarea:
                return t
        return None

    def editar(self, id_tarea, campo, nuevo_valor):
        #este edita el campo de una de las tareas nada mas
        tarea = self.obtener_por_id(id_tarea)
        if tarea:
            tarea.editar(campo, nuevo_valor) #si si son las mismas edita esos campos dentro de parentesis y guarda sino tira falso
            self.guardar()
            return True
        return False
    
    def eliminar(self, id_tarea):
        tarea = self.obtener_por_id(id_tarea)
        if tarea: #si te fijas es lo mismo que editar arriba, solo que ahora eliminas y usas siempre self, misma comparacion
            self.tareas.remove(tarea)
            self.guardar()
            return True
        return False
    
    #agregamos aqui porque en utils donde estaba usaba datos_globales osea codigo viejio
    #aqui esta ya usando los datos de la clase cabiar_Estado
    def cambiar_estado(self, id_tarea):
        tarea = self.obtener_por_id(id_tarea)
        if tarea:
            if tarea.estado == 'si':
                tarea.estado = 'no'
            else:
                tarea.estado = 'si'
            self.guardar()
            return True
        return False





        