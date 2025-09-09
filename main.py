from tasks import agregar_tareas


def mostra_menu():
    print("\n--- Menú Principal ---")
    print("1 - Agregar tareas")
    print("2 - Mostrar las tareas")
    print("3 - Salir")


def main():
    while True:
        mostra_menu()
        opcion = input("Seleccionar unas de las opciones \n")

        if opcion == '1':
            agregar_tareas()
            print("Haz seleccionado la opcion 1 ;)")


if __name__ == "__main__":
    main()