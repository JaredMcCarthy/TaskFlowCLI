from tasks import agregar_tareas, listar_tareas, tareas_completadas
import sys #exportando funcion para salir del programa

def mostra_menu():
    print("\n--- Menú Principal ---")
    print("1 - Agregar tareas")
    print("2 - Mostrar las tareas")
    print("3 - Salir")


def main():

    tareas_guardadas = []

    while True:
        mostra_menu()
        opcion = input("Seleccionar unas de las opciones \n")

        if opcion == '1':
            agregar_tareas(tareas_guardadas)
        elif opcion == '2':
            listar_tareas(tareas_guardadas)
        elif opcion == '3':
            tareas_completadas(listar_tareas)
        elif opcion == '4':
            print("Saliendo del programa...")
            sys.exit()




if __name__ == "__main__":
    main()