
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
    except ValueError:
        print("Ingresa valores que sean aceptados.")
    break
