
from tasks import datos_globales_dicc

from tasks import listar_tareas


def cambiar_estado():
	confirmacion = input("Desea cambiar el estado de una tarea? \n")

	listar_tareas()
	req_id = int(input("Ingrese el numero de tarea que quiere cambiar \n"))

	for i in range(int(datos_globales_dicc)):
		if i['ID'] == req_id:
			if datos_globales_dicc[i]['estado'] == 'si':
				datos_globales_dicc[i]['estado'] == 'no'
			else:
				datos_globales_dicc[i]['estado'] == 'si'
			print('Estado cambiado con exito.')
			break
	if not datos_globales_dicc[i]['estado']:
		print("No se encontro la tarea.")



def eliminar_tareas():
	listar_tareas()
	if datos_globales_dicc:
		try:
			indice = int(input("Ingrese el numero de la tarea a eliminar: "))
			if 0 <= indice < len(datos_globales_dicc):
				tarea_eliminada = datos_globales_dicc.pop(indice)
				print(f"Tarea {tarea_eliminada} eliminada")
			else:
				print("Numero de tarea no valido.")
		except ValueError:
				print("Entrada no valida. Poorfa ingrese un numero.")


