import random

tareas_global = []
random_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# random_letter = ["A", "E", "I", "O", "U"]

def agregar_tareas(agregdos):
    global num
    tareas_global.append(agregdos)
    for i in range(1, 10):
        num = random.choice(random_number)
    print(f"Se agrego la tarea num.{num} exitosamente.")
    tareas_global.append(listar_tareas)


def tareas_completadas(confirmacion=True):
    QA = input("Ingrese el codigo de la tarea completada? \n")
    print(QA)

    while confirmacion == True:
        ingreso_confirmacion = input("Quiere confirmar que este es el codigo?")

        try:
            if ingreso_confirmacion == "S":
                pass
        except ValueError:
            pass
        # Tomar codigo de tareas agregadas nada mas.
        #luego de eso que el usuario agregue done o no.


def listar_tareas(nueva_tarea, nueva_categoria, nueva_prioridad, nuevo_estado):
    if not tareas_global:
        print("No se han registrado tareas hasta el momento.")
    else:
        for i in enumerate(tareas_global):
            print({
                "Tarea": {nueva_tarea},
                "Categoria": {nueva_categoria},
                "Prioridad": {nueva_prioridad},
                "Estado": {nuevo_estado}
            })
