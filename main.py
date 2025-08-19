# hacer un menu para probar anandir tareas
# el objetivo es que el programa me deje agregar tareas y que se guarde en una lista de memoria

lista_global = []


class clase_principal:
    def __init__(self, tarea, category, prioridad, estado, ):
        self.tarea = tarea
        self.category = category
        self.prioridad = prioridad
        self.estado = estado


def menu_inicio():
    while True:
        print("\n--- Menú ---")
        print("1 - Agregar una tarea nueva")

        opcion = input("Porfavor seleccione una opcion.\n")

        try:
            if opcion == '1':
                tarea = input("Ingrese el nombre de la tarea.\n")
                category = input("Ingrese la categoria la categoria\n")
                prioridad = input("Ingrese la prioridad de la tarea.\n")
                estado = input("Ingrese el estado actual.\n")
                confirmacion = input("Desea confirmar las tareas? S/N\n")
                if confirmacion == "S":
                    objeto = clase_principal(tarea, category, prioridad, estado)
                    lista_global.append(objeto)
                    print("Los datos se han agreagdo a la lista.")
                    break
        except ValueError:
            print("Ingresa valores que sean aceptados.")
            break

menu_inicio()

for obj in lista_global:
    print(f"Tarea: {obj.tarea}, Categotia: {obj.category}, prioridad: {obj.prioridad}, estado: {obj.estado}.")
